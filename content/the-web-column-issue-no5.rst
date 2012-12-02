The Web Column: Issue No.5
##########################
:date: 2011-06-06 07:13
:category: blog
:tags: web-column

Welcome to issue number 5 - a.k.a the better late than never edition :).

.. contents::
   :class: rc



Recent news
===========

The latest news hot off the press.



Django | Weblog | Django 1.3 released
-------------------------------------

The latest iteration of the django web framework (one of the most popular ones) came out a couple of weeks ago. This release was delayed a few times but finally brings some much anticipated improvements: class-based views (cleaner view code FTW), better integrated logging, a standard way to handle static files and much more...

http://www.djangoproject.com/weblog/2011/mar/23/13/



Divide and Concur « Code as Craft
---------------------------------

Interesting article on Etsy&#039;s use of Jenkins to split up their test suite to get it run inside of 11 minutes pre-deployments.

http://codeascraft.etsy.com/2011/04/20/divide-and-concur/



The road to being a kick-ass public speaker | Christian Heilmann's blog – Wait till I come!
-------------------------------------------------------------------------------------------

Christian Heilmann provides some great insights and tips on what it takes to make a good presentation.

http://www.wait-till-i.com/2011/04/11/the-road-to-being-a-kick-ass-public-speaker/



byobu in Launchpad
------------------

Byobu is a fantastic set of enhancements to gnu screen. It provides a great deal of information and is on my list of base packages for any new machine.

https://launchpad.net/byobu



Puppet Labs - Style Guide
-------------------------

Puppet labs produce a style guide detailing exactly how your should layout your modules and manifests. Essential reading if you&#039;re using puppet and want to adhere to a common standard.

http://docs.puppetlabs.com/guides/style_guide.html



Fabric Gets a nice set of updates
----------------------------------
`Fabric <http://docs.fabfile.org/>`_, if you've not already heard of it is a python library that makes it really easy to handle deployments with a fabfile, which is essentially similar to a Makefile except that it it's just pure python.

Tav has built-out a bunch of additional features for Fabric: Running commands in parallel, API improvements, Fabric Shell. Staged environments. It's all there, the only downside is that it's not currently in a format that makes it easy for upstream to accept the patches. Still hopefully the work will be done to resolve that and we'll see these changes land in Fabric in due course. `See Tav's post for more details <http://tav.espians.com/fabric-python-with-cleaner-api-and-parallel-deployment-support.html>`_ (via `Ross Lawley <http://www.rosslawley.co.uk/>`_)



Iranian Hackers obtain SSL certs for major sites fraudulently
-------------------------------------------------------------------

An fairly worrying report from eff.org on how Iranian hackers managed to trick a Certificate Authority into issuing fraudulent SSL certs for major sites such as google.com, login.yahoo.com.

* `Iranian hackers obtain fraudulent HTTPS certificates: How close to a Web security meltdown did we get? <http://www.eff.org/deeplinks/2011/03/iranian-hackers-obtain-fraudulent-https>`_
* `Graham Cluely (Sophos) has more details on the incident <http://nakedsecurity.sophos.com/2011/03/24/fraudulent-certificates-issued-by-comodo-is-it-time-to-rethink-who-we-trust/>`_



Matt Haughey on 11 Years of Community at MetaFilter
-----------------------------------------------------

You may have seen this already but if not it's well worth seeing. Matt Haughey talks about the tools created to manage and moderate the community on MetaFilter.





Front-End
=========

Everything related to client-side development.


heatmap.js | HTML5 Canvas Heatmap Library
-----------------------------------------

Heatmaps are a fantastic way to visualise geographical statistics and of course user behaviour on web pages.
Heatmap.js is the easiest way I've seen to build such visualisations.

http://www.patrick-wied.at/static/heatmapjs/



jQuery: » jQuery 1.6 Released
-----------------------------

jQuery 1.6 is out, with small but major changes which break backwards-compatibility (see .prop() and .attr()).

This is not really a problem though, as jQuery has mostly been bug-free for a while, so running on 1.5 until you've updated your codebase, however big it is, is perfectly reasonable.

http://blog.jquery.com/2011/05/03/jquery-16-released/



Web font services - An Overview - by sprungmarker.de
----------------------------------------------------

Sylvia Egger keeps a useful comparison table of the various webfonts hosting services out there, allowing you to compare how many fonts are available, how you can embed them, what you can use them for and which particular services are offered.

http://sprungmarker.de/wp-content/uploads/webfont-services/



Anatomy of a Mashup: Definitive Daft Punk visualised
----------------------------------------------------

Cameron Adams awesome visualisation of his own audio mashup of 23 different Daft Punk tracks using modern web technologies.

http://daftpunk.themaninblue.com/



Improve Browser Performance With the CSS Stress Test Tool » SitePoint
---------------------------------------------------------------------

Bookmarklet that measures performance impact of CSS effects.

http://blogs.sitepoint.com/css-stress-test-tool/



An unconventional loading strategy for YUI 3 | Julien Lecomte's Blog
--------------------------------------------------------------------

An interesting deck from Julian Lecomte on YUI3 loading strategies used on SRPs.

http://www.julienlecomte.net/blog/2011/03/583/






Back-End
========

Server-side technologies and services.



The Secrets of Building Realtime Big Data Systems
-------------------------------------------------

Nathan Marz&#039;s presentation on building scalable architecture. This is a very good introduction to the type of architecture needed for any &quot;realtime&quot; analytics platform. Nathan has also written a few tools/libraries which facilitate data processing on Hadoop (for example Cascalog: https://github.com/nathanmarz/cascalog).

http://www.slideshare.net/nathanmarz/the-secrets-of-building-realtime-big-data-systems






The Python corner
=================

Python rocks. At Project Fondue, we love it and so we keep a close eye on what's happening in the Python realms. Here is an excerpt.



PyPy Status Blog: PyPy 1.5 Released: Catching Up
------------------------------------------------

A new release of Pypy is out and now claims to be on par feature-wise with Python 2.7.1 "including the standard library".

Pypy is a major achievement and keeps getting better and better. Don't gorget to check their compatibility list before you switch to it over cPython though: https://bitbucket.org/pypy/compatibility/wiki/Home

http://morepypy.blogspot.com/2011/04/pypy-15-released-catching-up.html


pyke
----

Pyke is a knowledge-based inference engine (expert system) written in 100% Python.

* `Pyke Homepage <http://pyke.sourceforge.net>`_
* Blog post with a practical application 
   * `In french <http://cyberdelia.tryphon.org/post/3291592720/moteur-inference>`_
   * `English Translation via translate.google.com <http://translate.google.com/translate?js=n&prev=_t&hl=en&ie=UTF-8&layout=2&eotf=1&sl=fr&tl=en&u=http%3A%2F%2Fcyberdelia.tryphon.org%2Fpost%2F3291592720%2Fmoteur-inference>`_

PyCon
------

There's a huge amount of fantastic videos of the talks from PyCon 2011. Well worth checking out.

`PyCon 2011 Videos <http://pycon.blip.tv/posts?view=archive&nsfw=dc>`_









