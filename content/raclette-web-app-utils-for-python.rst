Raclette: Web App Utils for Python
##################################
:date: 2009-07-14 10:58
:category: blog
:tags: wsgi, python

Something I've been working on for a while is consolidating the set of utilities that are used on our Python based sites. To start with this code was just a set of basic libraries that we've used alongside web.py.

It quickly became clear that this was something that could have more of a life of it's own. We've been finding WSGI to be a great thing for web application development because having a clear specification means that building apps and middlewares are far likely to be uttilsed because it doesn't matter which Python framework you use, whether it's a lightweight framework, Django, Pylons.

The goals for Raclette are to provide well tested middlewares and libraries that can be used to facilitate web development. We're also looking to keep the quality of code at a high standard as much as possible whilst balancing that with getting code out there so developers can try it out and provide feedback. 

raclette.gbs: Graded Browser Support Middleware
========================================================

The first app off the blocks is a WSGI middleware which provides a solution to implementing Yahoo's Graded Browser support strategy see http://developer.yahoo.com/yui/articles/gbs/ for more information.


Installation
------------

.. sourcecode:: Python

    sudo easy_install raclette.gbs

To use the middleware simply wrap the init of the middleware around your WSGI application

.. sourcecode:: python

    from raclette.gbs import GradedBrowser
    ...
    application = GradedBrowser(application)


raclette.gbs works by analyzing the user-agent string and returning a grade stating that the browser is C, A or X grade. Yahoo's own strategy only provides details of which browser's are A grade so the C grade matrix is pretty much created based on guess-work around the notion that C-Grade browsers should be Antiquated and rare.

Ultimately for the purposes of this middleware only C-grade browsers really need to be identified as A and X grade are generally treated the same. However to be able to give the end user more scope to do different things with browser grades in development or production C and A grades are explicitly identified. It's up to the user to modify the browser matrix should they wish to add or drop support for any particular browser.

Known Issues
------------

There's clearly some work to be done in terms of extending the data used to provide the decisions on which browsers are and aren't supported. With that in mind we're happy to get feedback on which browsers you think need to be indentified. Clearly it doesn't have to be something that's in Yahoo's matrix of support as it's clear that anyone using this may wish to define their own matrix of support.

Caching is not currently implemented. As the UA string is parsed on every request it's fairly crucial that caching is added - expect several caching solutions to be made available in subsequent releases.

Future Possibilities
--------------------

Something that came up early on was an idea around extending support to include some notion of graded mobile browser support in the sense that you might have MA, MX and MC. At this point it's not clear if having any separate grades for mobile devices is a good thing or not, but certainly being able to detect common mobile browsers would be useful.

Getting the code
-----------------

The code is available on launchpad.net at https://launchpad.net/raclette.gbs -- Contributions and patches gratefully received. All code is licensed under the modified BSD license.
