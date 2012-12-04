The Web Column: Issue No.2
##########################
:date: 2010-12-20 09:15
:tags: web-column
:category: blog

Welcome to the second issue of our "Web Column" series. A lot has been happened in the past week and you probably didn't have time to check your feeds every five seconds whilst Christmas shopping. Well here is our Christmas present to you then :) Enjoy!

.. contents::
   :class: rc

Recent news
===========

24 ways 2010 edition
--------------------

24 ways is carrying on with great articles about workflow, organisation, APIs and shiny Javascript and CSS techniques.

This year, 24 Ways is also printing all articles, selling it for £8 and donating all sales profits to UNICEF. Very cool.

- This year's 24 Ways is at http://24ways.org/2010/
- `Order an annual <http://fivesimplesteps.com/books/the-24-ways-annual-2010>`_ - hurry though; you can only order a copy during December!


Spacelog
--------

James Aylett and (ex-colleague) Mark Norman Francis regularly organise `/dev/fort <http://devfort.com/>`_, a week-long gathering of web geeks in an actual fort (yes!). Designers and developers alike collaborate without all the usual interference you can find in a "normal" office. Oh, and the Internet is a 30 minute walk away.

This year they launched Spacelog, a fantastic presentation of space mission transcripts from Nasa. Two missions are being featured so far: Apollo 13 and Mercury 6.

The UX, design and frontend work on this site are brilliant. It also offers very cool features like linkable transcript parts, for example http://apollo13.spacelog.org/05:03:12:07/05:03:12:35/#log-line-443527

- Stay up all night reading Spacelog at http://spacelog.org
- Don't miss Hannah Donovan's `article on 24 Ways detailing the process used during this year's /dev/fort. <http://24ways.org/2010/extreme-design>`_


Chrome Cr-48
------------

Google introduced a Pilot program for Chrome OS notebooks for US-based residents. Open until December 21st (Today!). It has been getting pretty good reviews all around. If they open up a program in Australia and the UK we'd be up for taking it for a spin :)

- http://www.google.com/chromeos/pilot-program-cr48.html
- http://www.slashgear.com/google-cr-48-chrome-os-notebook-review-20120389/
- http://www.wired.co.uk/news/archive/2010-12/10/first-look-google-netbook

WebSockets availability delayed
-------------------------------

You may have heard that Mozilla and Opera have announced that WebSockets won't be enabled by default in their future versions, due to a security issue with protocol. This is of course not very good news since WebSockets are pretty cool to play with and open up the door to a standardised way of implementing many new applications.

But do not fear, for this is not the end of WebSockets at all. Pusher, which develops a realtime communications platform based on WebSockets has all the details for you:

- http://blog.pusherapp.com/2010/12/9/it-s-not-websockets-it-s-your-broken-proxy

Prey: Open Source, Cross Platform Theft Recovery software
---------------------------------------------------------

Sadly Christmas time is well known to bring an increase in thefts of personal property. Prey is a nice bit of software which provides the means to activate tracking of your laptop or phone after it's been stolen (assuming you've installed it beforehand of course!).

It can do all-sorts of useful things such as reporting it's location based on wifi triangulation or gps if available as well as taking a photo of the thief if the device is equipped with a camera. Best yet Prey is cross platforma and is currently available for mac, windows, linux and android.

* http://preyproject.com/


Design
======

Retinart on page harmony
------------------------

Retinart, a beautiful design blog, has a great post of the Secret Law of Page Harmony, a pretty old technique to lay out elements on a page. They even give you the backstory behind the technique.

- http://retinart.net/graphic-design/secret-law-of-page-harmony/


Front-End
=========

CSS3 page curls
---------------

Page curls are quite shiny and Matt Hamm has come up with a nice example of how to make them using only CSS3.

- http://matthamm.com/box-shadow-curl.html


Framework activity
==================

Frameworks are built for The Greater Good ™. No matter which language or framework is your favourite, it's always good to be aware of what "the other guys" are doing. So here is what we picked up from the world of frameworks recently:


Django 1.3 getting there ...
----------------------------

... bit by bit. A few deadlines have been missed :( but things aren't that bad, and Django 1.3 is now scheduled for release at the end of January.

Django 1.3 will feature (amongst many other things) class-based views, improvements to logging and unit testing, and will deprecated mod_python support.

- the latest release schedule blog post: http://www.djangoproject.com/weblog/2010/dec/13/django-1_3-release-schedule-update/

Smisk: A Web-service framework written in C and controlled by Python
---------------------------------------------------------------------

Smisk is a framework for building scalable web-services using python. It's fully WSGI compliant and is currently being used in production by Spotify no-less.

* http://python-smisk.org/
* http://python-smisk.org/examples


The Python corner
=================

Python rocks. At Project Fondue, we love it and so we keep a close eye on what's happening in the Python realms. Here is an excerpt.

Configglue
----------

Configglue is a nice library that makes it really easy to combine both configuration files and command-line arguments. Fantastic for rolling utility scripts where the the amount of options can make the CLI-args seem a little unwieldy. There's also a separate project for using configglue to replace django settings.

* https://launchpad.net/configglue
* https://launchpad.net/django-configglue/
* http://packages.python.org/django-configglue/walkthrough/

Why PHP Is Fun and Easy But Python Is Marriage Material
-------------------------------------------------------

An interesting article which takes a look at programming language choices and more specifically deals with the pros and cons of PHP and Python. It makes some good points and is well worth a read if you're a PHP programmer thinking about getting into Python.

* http://onstartups.com/tabid/3339/bid/20493/Why-PHP-Is-Fun-and-Easy-But-Python-Is-Marriage-Material.aspx




Focus on: Python YQL
====================

Python-yql has recently become the newest Open Source project maintained by the Project Fondue Team so we'd thought it would be a good opportunity to highlight it.

If you've not heard of YQL (Yahoo Query Language) (you've probably been living under a rock) it's a SQL-like way to query the internetz for data from a growing number of public APIs. The nice thing about YQL is that it takes a lot of the effort out of interfacing with other APIs.

Python-yql is a Python wrapper to YQL which looks to make using YQL from Python as easy as possible. Here's a quick example of what you can do:

.. sourcecode:: python

    >>> from yql import Public
    >>> y = Public()
    >>> res = y.execute("""USE 'http://www.datatables.org/
    ukpostcode/ukpostcode.postcode.xml';
                        select * from ukpostcode.postcode
                            where postcode='SW1A1AA'
                                and format = 'xml'""")
    >>> res.one()['geo']['lat']
    u'51.501007'
    >>> res.one()['geo']['lng']
    u'-0.141588'
    >>>


* Python-yql documentation: http://python-yql.org
* Python-yql Launchpad Project: https://launchpad.net/python-yql

Python-yql has been around for about a year, and there's been quite a few updates in that time. However we're always happy to hear from anyone with suggestions or feature requests. If you have found a bug or something doesn't work how you'd expect it to please file a bug on launchpad - https://launchpad.net/python-yql. Additionally patches are welcomed.

End of Year!
=============

Ok, that's it! Join us again in the new year for the next edition of the web column. We're going to retreat to our Mountain hideaway over the Christmas holidays to eat fondue, drink and be merry. Here's wishing you all very happy Christmas and a happy new year!

