The Web Column: Issue No.4
##########################
:date: 2011-02-09 09:23
:tags: web-column
:category: blog


Welcome to issue number 4. Wow January flew by didn't it? It'll be summer before we know it. This week we have a bit of a hoo-hah over Google's accusation that Bing have been improving their search results by taking a look over Google's shoulder. We have deferreds in JQuery, some HTML 5 form action and a cautionary tale about relying on JavaScript for navigation alongside other web-related links fresh from the internetz.

.. contents::
   :class: rc

Recent news
===========

The latest news hot off the press.


Google Accuses Bing of Copying their Search Results
---------------------------------------------------

A fascinating article by Danny Sullivan that broke the news on Google's accusation that Bing are copying their search results.
`Google Accuses Bing of Copying their Search Results <http://searchengineland.com/google-bing-is-cheating-copying-our-search-results-62914>`_


Why You Should Never Search For Free WordPress Themes...
--------------------------------------------------------

Want a free wordpress theme? You might be getting more than you bargained for.  `This article looks at various sites that provide free wordpress themes only to uncover a whole heap of obfuscated spam. <http://wpmu.org/why-you-should-never-search-for-free-wordpress-themes-in-google-or-anywhere-else/>`_. Talk about there being no such thing as a free lunch.


History Hack Day
-----------------

YDN's Murray Rowan reports on the events at the recent `History Hack Day <http://developer.yahoo.com/blogs/ydn/posts/2011/01/history-hack-day-it-was-therefore-it-now-isnt/>`_. Sounds like it was a great success with many excellent hacks being produced over the course of the event.

    "Hack Days get people engaged with and excited about a subject, and our subject is history. There's a lot of it about, but lots of it is stuck, on paper, in old HTML pages, in archives, on hard-to-reach databases. We want people to figure out how to set some of that free, and start bringing that history to life as... whatever crazy things people can come up with."
    
    -- `Matt Patterson, Organiser of the History Hackday <http://historyhackday.org/>`_


Spread the Word on Facebook Scams and Phishing Techniques
---------------------------------------------------------

`Graham Cluley's Naked Security blog <http://nakedsecurity.sophos.com/>`_ is a great resource for keeping abreast of the latest news relating to computer/web security. Recently a lot of the news has been related to scams on facebook. 

Now for those of us who work in the industry it might be more easy for us to spot a scam from a mile away. However if you have friends and family that frequent facebook and similar sites it could be worth getting them to take a look at Graham's blog to understand how theses ploys work and how they generate scammers money.



Front-End
=========

Everything related to client-side development.


Deferreds in JQuery 1.5
------------------------

`Using deferreds in Jquery <http://www.erichynds.com/jquery/using-deferreds-in-jquery/>`_ provides a nice walk through of how to use the new feature in JQuery 1.5. 

    "With deferreds, multiple callbacks can be bound to a task’s outcome, and any of these callbacks can be bound even after the task is complete. 
    The task in question may be asynchronous, but not necessarily."

    -- Eric Hynds

If you've ever used Twisted in Python this territory will be familiar to you.


HTML5 Forms
-----------

Chris Mills and Patrick H. Lauke provide walk through some of the shiny new HTML 5 features available for creating richer forms on Dev.Opera: `New form features in HTML5 <http://dev.opera.com/articles/view/new-form-features-in-html5/>`_


Breaking the Web with HashBangs
-------------------------------

Mike Davies writes up an excellent critique on the trend of using fragment identifiers to provide state for Ajax based site navigation schemes. `Breaking the Web with Hashbangs <http://isolani.co.uk/blog/javascript/BreakingTheWebWithHashBangs>`_


Little big details
------------------

Quite often the work going into improving the user experience goes unnoticed even though it can turn on ordinary application or web site into something users actually enjoy. You know, that whole "delight your users" thing.
`Little big details <http://littlebigdetails.com>`_ is a blog pointing out those improvements and sometimes genuinely innovative ideas that make the software we like using.



Back-End
========

Server-side technologies and services.


Elasticsearch
-------------

As explained on the homepage, search is hard. That's exactly the problem `elasticsearch <http://www.elasticsearch.org>`_ is trying to tackle, and by the looks of things it might be successful at making search a lot more trivial than it currently. Many features one might expect from a robust search solution have been implemented in elasticsearch and quite often requiring little work or no work at all for the user: redundancy, failover, multiple indices, easy data format, simple configuration, automatically distributed architecture, choice of index storage etc.

We haven't tested it ourselves (yet), but this looks like an impressive project with a lot of potential. If you're looking at implementing search: give elasticsearch a go.




The Python corner
=================

Python rocks. At Project Fondue, we love it and so we keep a close eye on what's happening in the Python realms. Here is an excerpt.

datadiff
--------

This is an interesting idea. `Datadiff <http://pypi.python.org/pypi/datadiff>`_ provides a way to get a human readable diff from python data structures

.. sourcecode:: python

    >>> from datadiff import diff
    >>> a = dict(foo=1, bar=2, baz=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> b = dict(foo=1, bar=4, baz=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    >>> print diff(a, b)
    --- a
    +++ b
    {
    -'bar': 2,
    +'bar': 4,
     'baz': [
     @@ -5,11 +5,8 @@
      6,
      7,
      8,
     -9,
     ],
     'foo': 1,
    }

Grin and Search it
-------------------

`Brandon Craig Rhodes <http://rhodesmill.org/brandon/2011/grin-and-search-it/>`_ uses `grin <http://pypi.python.org/pypi/grin>`_ instead of grep. It's fairly similar to ack-grep but is written in python.

grin provides a way to search through files, colorising the matches in the output so you can see exactly what you were looking for and quickly.



