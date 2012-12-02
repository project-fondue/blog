Using Apache in a Python Development Environment
################################################
:date: 2010-07-12 22:21
:category: blog
:tags: apache, mod_wsgi, python

Making a development environment as close to the what's used in production is always a good plan, as it helps to catch issues earlier as you develop. The following details the way we are using apache in the development of a current side-project.

.. figure:: http://pf.staticfil.es/blog/images/apache-dev.png

    figure 1: Apache front-end and two web services.

Initially our development environment used the built-in WSGI server that comes with Werkzeug, but it occurred to me that ultimately this would be running on `mod_wsgi <http://code.google.com/p/modwsgi>`_ under apache, so we decided to set-up the development environment to use apache instances with mod_wsgi running in daemon mode.

This actually proved to be fairly straight forward, all that's required is to generate a configuration for each instance at run-time, which points at each application.

By abstracting the start-up of each instance a single script can fire up the web-services, and additionally the front-end one after the other. The other advantage with this approach is that you can then develop any configurations that make use of apache modules with ease, so for example using something like mod_rewrite is no problem. In essence this means you don't have to write utility code that's just used to replicate something that your server provides.

Reloading on changes. Development servers such as Werkzeug's come with code to trigger a reload when code changes so that you can see changes instantly during development. Fortunately with mod_wsgi this isn't a problem as the code is provided for you see `the mod_wsgi documentation <http://code.google.com/p/modwsgi/wiki/ReloadingSourceCode>`_.

Configuring this as part of the environment is simple and works very well.

All of this means you can have a development evnironment that brings you closer to a production environment with minimal hassle. So far this is working very well for us.
 

