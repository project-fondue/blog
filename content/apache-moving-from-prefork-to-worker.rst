Apache: Moving from prefork to worker
#####################################
:date: 2010-03-04 23:23
:tags: apache
:category: blog


In this post we look at the results of moving our Apache from mpm-prefork to mpm-worker for Python based web-apps in an attempt to reduce memory usage.


Differences between MPM Versions
--------------------------------

So what are the differences between Apache MPM ("multi-processing module") types?

MPM Prefork doesn't use threads and instead spawns child processes to serve requests. MPM Worker on the other hand uses multi-threaded processes where each child process utilises a number of threads:

     By using threads to serve requests, it is able to serve a large number of requests with less system resources than a process-based server. Yet it retains much of the stability of a process-based server by keeping multiple processes available, each with many threads.
     
     -- Apache 2 Documentation

Something to bear in mind is that you probably won't want to switch to worker if you are using PHP unless you are ok with using PHP as FastCGI and even then the `PHP manual doesn't recommend using MPM worker. <http://www.php.net/manual/en/faq.installation.php#faq.installation.apache2>`_

For us that means we are now running our PHP apps using prefork and mod_php on a box dedicated to running PHP. This is better in a lot of ways because it means we can tune Apache for each specific application rather than running a mixture of PHP and Python apps on the same hardware.

Converting to mpm-worker
------------------------

Actually carrying out the conversion on an Ubuntu box is as simple as running

.. sourcecode:: sh

    sudo apt-get install apache2-mpm-worker

That will remove prefork if you have it installed and will install worker in its place and trigger a restart. That's all there is to it. (Though of course YMMV)


What Difference does it make?
-----------------------------

In our case used memory levels dropped a reasonable amount as you can see in the last 6th of this graph:

.. image:: http://pf.staticfil.es/blog/images/radha.png
   :alt: Graph Showing memory usage down when switched to MPM worker


Related Reading
_______________

* `Pushing Apache Performance <http://lucumr.pocoo.org/2007/9/30/pushing-apache-performance>`_
* `Multi-Processing Modules (MPMs) <http://httpd.apache.org/docs/2.2/mpm.html>`_

