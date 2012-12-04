Building a Static Asset Cluster
###############################
:date: 2010-02-11 23:22
:category: blog
:tags: glusterfs, haproxy, nginx, scaling

At Project Fondue we've always used the venerable Apache for our webserver and up until now we didn't have anything special set-up for serving static assets. For a while now I've wanted to move to using Nginx to serve static content as it's generally considered to perform well, it's nice to use and has a low memory footprint.

In this post we take a look at what software was used to build this set-up and how it all goes together.

Initial Thoughts
================

As this configuration is going to be used by several sites it became clear that building some kind of redundancy into the setup would be a good idea. Otherwise if this ended up as a single point of failure, all our sites would have no images, JavaScript or CSS should something go wrong with the static server.

So the first piece in the puzzle was being able to share a single public ip address across 2 Slicehost boxes to provide high availability. We're using the excellent `Slicehost <http://slicehost.com>`_ as our provider and they're happy to support HA configurations. For a shared IP address all it takes is a mail to Slicehost support to say that's what you want. At the same time I added another public IP so that each box has a dedicated local network and public IP address as well as sharing a single public ip between them.

.. figure:: http://pf.staticfil.es/blog/images/haproxy-nginx-glusterfs.png

    figure 1: Basic diagram showing simple static cluster across 2 boxes.

Setting up Heartbeat
====================

Setting up heartbeat [#heartbeat]_. is an extremely straightforward process it's simply a case of installing the packages and then providing configs for each box as well as a centralised config which is the same on both boxes.

The way it works is that one box has the shared IP enabled on an alias of the primary network card eth0 in our case. If the non-live server detects the live box has gone down it switches on its alias for the shared IP address. This provides a quick and easy way to have failover. Slicehost provide detailed instructions on using Heartbeat with slices on their site [#slicehostha]_.

Setting up HAProxy
==================

The next piece is HAProxy [#haproxy]_ which we use as a load balancer. This handles all the traffic on port 80 and then balances it across our Nginx boxes which are serving from port 8080. HAProxy requires some fairly simple configuration where you define a farm and define the nodes you want to balance traffic over. If you are balancing traffic for an application it's possible to have HAProxy set cookies so that once a client has made one request all subsequent requests will go to the same box. In our case we are dealing with static content so it's not necessary.

.. sourcecode:: haproxy

    server  Static1 xxx.xxx.xxx.xxx:8080 check port 8081 inter 2000
    server  Static2 xxx.xxx.xxx.xxx:8080 check port 8081 inter 2000

So that HAProxy knows which of our Nginx boxes are up, it uses a HEAD request to each machine to check it's alive. This is carried out on a separate port e.g: 8081 so that it's independently controlled. Done this way we can switch off the Nginx config (via a script nginxdissite) in order to temporarily remove it from the farm. An alternative to this would be to turn off access to port 8081 through iptables. Either way; this makes it dead easy to be able to carry out maintenance without removing all static serving capabilities. Adding it back in is just a case of re-enabling the site and then HAProxy can start distributing traffic to that node again.

HAProxy also comes with a stats page which you can view as a way of being able to see what nodes are up and how much traffic is being served at any one time.

Configuring Nginx
==================

The Nginx [#nginx]_ configuration is pretty straightforward in that it's optimised for static asset serving and defines GZIP and Expires along with a couple of custom rewrite rules. The first is to allow Nginx to discard version numbers from requests. This is a cache-busting mechanism for when assets are set with long expiry date of a year in the future. The only way to get the client to download a new asset (when for example a graphic has been altered or CSS updated) is to provide a new URI. This is done by adding the revision to the asset file name. So rather than linking to `/i/foo.png` we can link to `/i/foo.2348.png`.

.. sourcecode:: nginx

    rewrite "^(.*)\.\d+\.(jpeg|jpg|gif|png|css|js|html)$"  $1.$2;

The second rewrite addition is to redirect subdomains to directories. This provides a nice easy way to be able to utilise new subdomains in the future depending without needing to update the configuration. This of course requires a wildcard A record to be set up in DNS as well as a wildcard in the server_name directive.

.. sourcecode:: nginx

    if ($host ~ '(.*)\.staticfil.es' ) {
        set $subdomain $1;
        rewrite  "^/(.*)$"  /$subdomain/$1;
    }

Lastly I wrote my own nginxensite/nginxdissite for enabling and disabling configurations. This is based on the same Debian/Ubuntu convention used with Apache. The Apache convention is the following: you have sites-enabled and sites-disabled directories and the sites-enabled directory is set-up so that any configuration within it is automatically included. The a2ensite command symlinks a chosen configuration from sites-available into sites-enabled. The benefit of it is that it encourages good separation of a conf for each site and provides a quick way to drop a particular configuration or replace it with a new one.

Mirroring Static Assets with Glusterfs
======================================

The final issue with setting something like this up is how to cleanly share assets between servers. A basic solution would be to use rsync on cron which is fine, except that there would be a delay between getting files on one box before it is synced to the other one. To eliminate this delay I considered writing a script based on inotify which would run rsync as files were added but this would also create lots of problems to solve, such as ensuring adding lots of files doesn't result in too many rsync processes, but at the same time doing this without losing the almost realtime aspect of delivery which is the desirable result.

I then started looking into what was available from distributed filesystems.  In the end after some testing I settled on using Glusterfs [#glusterfs]_. Glusterfs has a server and a client component and is very easy to set-up. In our case I made the two boxes run the server configuration which essentially makes each node a mirror of the data. Then each server also runs the client which is essentially a mount of the filesystem via FUSE [#fuse]_. Adding files through the client makes those files almost instantaneously available from both static servers which is perfect for what we are trying to do. The other cool thing with Gluster is that scaling this up through adding more boxes becomes very easy to do.

Glusterfs is also fault tolerant in that if we drop one of the servers out of the farm for maintenance and continue to add files to be served as soon as that box is back in rotation it will pick up all of the missing files.

So that's it's - feel free to add your thoughts, comments, experiences of this kind of set-up or similar in the comments.

Related Links
-------------

.. [#heartbeat] HeartBeat Failover http://www.linux-ha.org/wiki/Heartbeat
.. [#slicehostha] Setting up ip failover on slicehost http://articles.slicehost.com/2008/10/28/ip-failover-slice-setup-and-installing-heartbeat
.. [#haproxy] HAProxy http://haproxy.1wt.eu/
.. [#nginx] Nginx http://wiki.nginx.org/
.. [#glusterfs] Gluster File System http://www.gluster.org/
.. [#fuse] Filesystem in User Space http://en.wikipedia.org/wiki/Filesystem_in_Userspace


