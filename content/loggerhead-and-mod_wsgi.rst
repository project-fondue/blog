Loggerhead and mod_wsgi
#######################
:date: 2009-11-26 09:14
:tags: apache, loggerhead, mod_wsgi, python, wsgi
:category: blog

We've recently started using Loggerhead for branch browsing as the redmine support for bazaar is a little lacking. We also wanted to provide a way to expose our open-source projects to the world.

Currently `loggerhead <https://edge.launchpad.net/loggerhead>`_ defaults to using pasteserver out of the box, which means you have to proxy this with Apache if you don't want to use pasteserver directly. Instead of doing that we went the route of setting up Loggerhead under apache with mod_wsgi.

Here's the wsgi file to set-up the application.

.. sourcecode:: python

    BZR_SERVE_DIR = 'THE_DIR_CONTAINING_YOUR_BRANCHES_HERE'

    import sys
    import os
    sys.path.insert(0, os.path.dirname(__file__))

    from paste.httpexceptions import HTTPExceptionHandler
    from loggerhead.apps.transport import BranchesFromTransportRoot
    from loggerhead.apps.error import ErrorHandlerApp
    from loggerhead.config import LoggerheadConfig
    from paste.deploy.config import PrefixMiddleware
    from bzrlib.plugin import load_plugins

    load_plugins()
    config = LoggerheadConfig()
    app = BranchesFromTransportRoot(BZR_SERVE_DIR, config)
    app = PrefixMiddleware(app, prefix='/')
    app = HTTPExceptionHandler(app)
    application = ErrorHandlerApp(app)


I save this file as loggerhead.wsgi in the checkout of loggerhead.

Next all you need is a basic apache config and a WSGIAlias directive pointing at the wsgi file. Obviously it goes without saying this example is just for illustrative purposes.


.. sourcecode:: apache

    <VirtualHost *:80>
        ServerName loggerhead

        WSGIScriptAlias / /PATH_TO_LOGGERHEAD/loggerhead.wsgi

        <Directory /PATH_TO_LOGGERHEAD>
            Order allow,deny
            Allow from all
        </Directory>

    </VirtualHost>


.. note::

    The following assumes you have a dns entry for whatever value you give ServerName - In my example I use loggerhead which I have set-up on my local machine to point to 127.0.0.1 so I have a local loggerhead running to view my checkouts.

* Change the values of the paths and the ServerName as necessary
* Save this file as loggerhead (or whatever you want to call it) in /etc/apache2/sites-available

Then all you need to do is enable it with

.. sourcecode:: sh

    sudo a2ensite loggerhead
    sudo /etc/init.d/apache2 force-reload

That's it!

You can view our code repository at http://code.projectfondue.com/ and a branch for these files is here: http://code.projectfondue.com/loggerhead-wsgi/trunk/files




