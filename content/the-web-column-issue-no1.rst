The Web Column: Issue No.1
##########################
:date: 2011-01-14 09:13
:tags: web-column
:category: blog

This is the first post in our "Web Column" series, detailing recent activity in the web development field that might be relevant to you. Posts like this will appear regularly to keep you up to date with important webdev news.

.. contents::
   :class: rc

Recent news
===========

24 ways 2010 edition
--------------------

For the 6th year in a row, Drew McLellan and friends are back to make December the best month of the year.

The 2010 edition is already packed with progressive enhancement, web fonts, Javascript, CSS, design goodness, and generally good advice, as usual.

- Drop whatever you're doing and go read it at http://24ways.org/2010/. Now!


CSS3 Flexible Box Layout Module
-------------------------------

In the same spirit, Robert Nyman has a great article and examples about the CSS3 Flexible Box Layout Module.

This is something many frontenders have been wishing for, and now it's just around the corner (the IE and Opera teams still need to work on it).

- Robert's article: http://robertnyman.com/2010/12/02/css3-flexible-box-layout-module-aka-flex-box-introduction-and-demostest-cases/


JSMentors mailing list
----------------------

Rey Bango and Asen Bozhilov decided to put together a list dedicated to all things Javascript, including reviewing code and getting by some of the best JS coders out there. If you don't feel up to scratch on JS, this might be one of the best places to find good advice.

- The mailing list's site: http://jsmentors.com
- The announcement at Ajaxian: http://ajaxian.com/archives/jsmentors-com-the-mailing-list-to-learn-javascript


New Web Messaging working draft
-------------------------------

A new working draft has been published by Ian Hickson regarding communication between different browsing contexts (ie. documents) "regardless of their source domain".

Of course security measures are part of the spec, which still states "Warning! Use of this API requires extra care to protect users from hostile entities abusing a site for their own purposes."

Don't let that scare you too much and keep on eye on this spec though, as communication between different web pages would be a big deal if vendors start to implement it.

- The draft is at http://www.w3.org/TR/2010/WD-webmessaging-20101118/


CSS railroad diagrams
---------------------

Stoyan Stefanov has decided to "enjoy his unused vacation days" writing a CSS parser in Javascript. Yep.

After writing a lexer, he's now taking on the parsing task and details his work in a set of railroad diagrams which will give you a little bit of insight into what work browsers have to do upon page load.

- The lexer code: https://github.com/stoyan/etc/tree/master/cssex
- Post about parsing, with railroad diagrams: http://www.phpied.com/css-railroad-diagrams/


MobileSafari and HTML5
----------------------

iOS 4.2 came out recently, with a new version of Mobile Safari and new features: accelerometer, Web sockets, HTML5 Forms, partial XHR2 support and better JS, DOM, SVG and Canvas support.

- You can find a good list of the changes at http://www.mobilexweb.com/blog/safari-ios-accelerometer-websockets-html5


Apparently XHTML 2 is still around
----------------------------------

Oh well...

- http://www.w3.org/News/2010.html#entry-8962


Smashing Magazine roundup of project questionnaires
---------------------------------------------------

If you do freelance work, or even work for an agency, understanding what your clients actually want isn't always that simple.

I always found Clearleft's Client Ideas Sheet was great, but Smashing Magazine went around and did a round up of many questionnaires of this kind. From all these you can probably compile your own that fits your type and style of work. Very useful stuff.

- http://www.smashingmagazine.com/2010/11/26/web-design-questionnaires-project-sheets-and-work-sheets/



Framework activity
==================

Frameworks are built for The Greater Good ™. No matter which language or framework is your favourite, it's always good to be aware of what "the other guys" are doing. So here is what we picked up from the world of frameworks recently:


OpenSocial 1.1 published
------------------------

The OpenSocial spec is carrying on with version 1.1 published in November, with emphasis on pub/sub communication between gadgets.

- http://blog.opensocial.org/2010/11/opensocial-11-published.html


Backbone.js and Django
----------------------

Josh Bohde has a nice example of how to integrate Backbone.js with Django.

- http://joshbohde.com/2010/11/25/backbonejs-and-django/


DjangoCon US 2011 announced
---------------------------

From the blog post: "DjangoCon US 2011 will be held in Portland, Oregon, from September 6-8 2011. This will be followed by a couple of days of sprints."

A couple of things to note: the venue has changed, and the organizers are calling for help via their mailing list.

- Announcement: http://www.djangoproject.com/weblog/2010/nov/22/djangocon-us-2011/
- Organizers' mailing list: http://groups.google.com/group/djangocon-organizers


Rails for Zombies
-----------------

In order to make Rails fun to learn, the guys at Envylab came up with a pretty cool educational concept: "You'll watch five videos, each followed by exercises where you'll be programming Rails in your browser."

Oh, and the whole thing has a Zombie theme.

- The site: http://railsforzombies.org


Symphony 2 is making good progress
----------------------------------

A whole lot of work was checked in recently and apparently it could hit beta before the end of the year.

- Summary of recent activity: http://www.symfony-project.org/blog/2010/11/28/a-week-of-symfony-204-22-28-november-2010



The Python corner
=================

Python rocks. At Project Fondue, we love it and so we keep a close eye on what's happening in the Python realms. Here is an excerpt.


Textmate and Pyflakes
---------------------

David Crammer wanted inline-error checking in Textmate and made a bundle for it, based on an existing one for Javascript.

- Blog post: http://www.davidcramer.net/code/36327/integrating-pyflakes-into-textmate.html
- Javascript Tools Bundle: https://github.com/johnmuhl/javascript-tools-tmbundle
- David's Python Tools Bundle: https://github.com/dcramer/python-tools-tmbundle


Yahoo! Pipes, Python and Appengine
----------------------------------

Greg Gaughan, inspired by others, has decided to compile Yahoo! Pipes into Python code and run them on AppEngine.

- Blog post: http://www.wordloosed.com/running-yahoo-pipes-on-google-app-engine
- The code on Github: https://github.com/ggaughan/pipe2py
- The test site, on AppEngine: http://pipes-engine.appspot.com


Twisted 10.2.0 out
------------------

From the announcement: "Survivors of the release process - what few there were of them - have been heard to claim that this version is "awesome", "even more robust", "fun-sized" and "oven fresh"."

There's no reason not to use it then.

- Announcement: http://labs.twistedmatrix.com/2010/11/twisted-1020-released.html
- Twisted's site: http://twistedmatrix.com


Python redis graph library
--------------------------

Amir Salihefendic has implemented a small graph library on top of Redis.

- Blog post: http://amix.dk/blog/post/19592#redis-graph-Graph-database-for-Python
- The Package on Pypi: http://pypi.python.org/pypi/redis_graph/1.0


PySignals
---------

Django implements signals as a nice way to achieve decoupling through your site.

Theo Julienne extracted that signal dispatcher into its own package and put it on Pypi. Good idea!

- The Package on Pypi: http://pypi.python.org/pypi/pysignals/0.1.1


Mongrel and WSGI apps
---------------------

A new WSGI handler for Mongrel was published by Daniel Holth. This adds to the existing "Mongrel2-WSGI-Handler" by Berry.

If you wanted to play with Mongrel2 and Python, you're all sorted now.

- http://bitbucket.org/dholth/mongrel2_wsgi
- https://github.com/berry/Mongrel2-WSGI-Handler


Scrapemark
----------

Scrapemark is a nice little module that lets you easily scrape web pages. 

- The site: http://arshaw.com/scrapemark/



Focus on: Object Oriented CSS Framework
=======================================

In most issues, we will spend a bit more time detailing a particular, not necessarily new, project which we deem particularly useful and might not be known from all.

This time: Nicole Sullivan's Object Oriented CSS Framework (OOCSS for short).

Through 2008 Nicole developed the idea of a simple, highly reusable and maintainable way of writing CSS code. At the beginning of 2009 she pushed the first public commit of the OOCSS project.

OOCSS emphasises the importance of separation between the structure and the styling (or "skin"). It also ensures that most "objects" can be embedded in most containers. You've certainly wanted to move a piece of functionality from one location to the other on a page before. Writing your CSS with OOCSS makes this process a lot simpler than it usually is.

Oh and of course, reusability for you as a developer, means reusability by the browser too. Less parsing is always good for performance.

OOCSS is not a massive framework of sorts. It is, essentially, a way of working that comes with examples. It advocates a change in mindset: what you usually see as a set of technical properties and attributes, coded in a linear way, element after element, you should try to see as functional, logical blocks and then organise your code as so.

Looking at the big picture is rarely a waste of time, and what you will gain is clarity both in your head and in your code.

You can certainly apply principles of OOCSS through your work without necessarily using the provided templates. But toying around with the code on Github doesn't hurt and will at least show you the way all this can be achieved.

Give it a go, if you don't adopt it, you'll probably learn from it.

- Public site: http://oocss.org (apparently put together for the Velocity conference)
- The code on Github: https://github.com/stubbornella/oocss
- The wiki on Github: https://github.com/stubbornella/oocss/wiki
- Nicole's post introducing OOCSS: http://www.stubbornella.org/content/2009/02/28/object-oriented-css-grids-on-github/





