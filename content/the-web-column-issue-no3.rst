The Web Column: Issue No.3
##########################
:date: 2011-01-18 10:10
:tags: web-column
:category: blog

Welcome to the third issue of our "Web Column" series. We trust you've had a relaxing Christmas break and are already enjoying the start of 2011. We've had a little bit of a spring clean around here and have carried out a little "refresh" of this site to make things a bit easier to read and provide more of a sense of space.  We hope you like it.

.. contents::
   :class: rc

Recent news
===========

Google Drops Native support for H.264 from Chrome
-------------------------------------------------

There's been a strong reaction to the news that Google is dropping native support for the H.264 codec within Google Chrome in order to push forward their own open-source `WebM <http://www.webmproject.org/>`_ codec. There's plenty of polarised opinons, and that's not suprising with Apple and Microsoft in one corner and Opera, Mozilla and Google in the other (`see this chart from Bruce Lawson <http://www.flickr.com/photos/24374884@N08/5349656086/>`_).

* daringfireball.net - `Google Dropping Support for H.264 in Chrome <http://daringfireball.net/linked/2011/01/11/h264-chrome>`_
* wired.com - `Google Reveals Plan To Remove H.264 Support From Chrome <http://www.wired.com/epicenter/2011/01/google-reveals-plan-to-remove-h-264-support-from-chrome/>`_

Puppet Cookbook Launched
------------------------

Former colleague `Dean Wilson <http://www.unixdaemon.net/>`_ has been hard at work over the break putting together the `Puppet Cookbook <http://www.puppetcookbook.com/>`_ - It's full of sound tips and definitely a resource worth keeping tabs on if you're using Puppet for configuration management.

Why developers should care about system packages
------------------------------------------------

In `Why developers should care about system packages <http://morethanseven.net/2011/01/16/Why-developers-should-care-about-system-packages.html>`_ Gareth Rushgrove details why system packages are important and why packaging skills are important for developers to learn. He also mentions Launchpad's excellent PPA feature, which is something we use quite a bit here at Project Fondue for backporting newer package versions. Back-porting a newer version of a package is something that PPA's are really handy for. Particularly as with a lot of packages this is often a relatively simple task.


How Facebook Ships Code
-----------------------

Whether you like the site's purpose or not, there is no denying that Facebook is a high traffic, technically challenging site. `These rumors <http://framethink.wordpress.com/2011/01/17/how-facebook-ships-code/>`_ on how Facebook handles development and deployment are of course to take with a grain of salt, but can provide a little insight into how different a company Facebook might be, should you care.


Bazaar Pipeline Plugin Demo
----------------------------

`Bazaar Pipeline Plugin Demo <http://bazaarvcs.wordpress.com/2011/01/16/bzr-pipelines-demo-video/>`_ provides a run-through of what can be achieved with the `bzr-pipeline plugin <http://wiki.bazaar.canonical.com/BzrPipeline>`_. Which looks potentially very useful for breaking up large projects in to smaller bite-sized, reviewable chunks.


Google App Engine's new High Replication Datastore
--------------------------------------------------

`Google has announced that it will now support a second datastore for App Engine <http://googleappengine.blogspot.com/2011/01/announcing-high-replication-datastore.html>`_ as a remedy to availability problems encountered with the regular Master/Slave datastore. There are a few caveats though:

- an application has to take particular precautions when using this new High Replication datastore, particularly regarding write latency, which can be much higher than before. Therefore data consistency is not guaranteed as much as it was with the Master/Slave datastore.
- the new duplicates data across many data centers, which means more bandwidth used by Google, which in turn means the pricing of this new datastore is significantly higher than its little brother's. Google is starting with a three times more expensive scheme and will re-evaluate the price in June.

Despite its drawbacks, the new datastore seems like a pretty robust offer.
If you value Google App Engine as your hosting platform of choice and should avoid downtimes at all cost, this might just be the solution you were waiting for.


Front-End
=========

NoVNC 
----- 
`NoVNC <http://kanaka.github.com/noVNC/screenshots.html>`_ - An exciting project which provides VNC with HTML5, websockets and canvas. via `@sil <http://twitter.com/sil>`_


Modernizr 2.0 Beta Preview
--------------------------

Faruk Ate? and Paul Irish have joined forces with Alex Sexton to put out `a 2.0 version of Modernizr <http://modernizr.github.com/Modernizr/2.0-beta/>`_, their feature detection Javascript library, which "allows you to target specific browser functionality in your stylesheet". This is a very handy tool when using a progressive enhancement approach, which you already do, of course...


Game development and Javascript
-------------------------------

A `very long list of game development resources in Javascript <http://www.reddit.com/r/javascript/comments/f094j/list_of_js_game_engines_community_effort/>`_ was compiled on Reddit. You can find there a plethora of graphics and audio engines to play with. With WebGL being implemented across most modern web browsers at the moment, game development will soon become a new avenue for your leet JS skillz :)



Framework activity
==================


Symphony 2
----------

Work on Symphony 2 `is continuing with recent refactoring (and more) <http://www.symfony-project.org/blog/2011/01/16/a-week-of-symfony-211-10-16-january-2011>`_ and `a PR5 release <http://www.symfony-project.org/blog/2011/01/17/symfony2-pr5-released>`_ which Fabien Potencier said is more or less the equivalent to a beta release. A release candidate is planned soon.


DjangoCon Europe 2011
---------------------

`DjangoCon Europe 2011 was recently announced <http://www.djangoproject.com/weblog/2011/jan/14/djangocon-eu-2011-announced/>`_ and will take place in June in Amsterdam, in the old port district (a pretty cool and different area). All the relevant info can be found `at the official site <http://www.djangocon.eu>`_.



The Python corner
=================

Python rocks. At Project Fondue, we love it and so we keep a close eye on what's happening in the Python realms. Here is an excerpt.

Ned Batchelder: Faked translations: poxx.py
-------------------------------------------
`poxx.py <http://nedbatchelder.com/blog/201012/faked_translations_poxxpy.html>`_: A Nice utility for testing out gettext translations.


Pyro
----

`Pyro <http://www.razorvine.net/python/Pyro>`_ stands for Python Remote Object library and does exactly that: let you call Python code running on other machines. The API is very simple and a new version, Pyro 4, is being written from scratch at the moment. RPC can be a tedious task, so there is no doubt this could come as a handy tool to quite a few people.



Focus on: WTForms
=================

`WTForms <http://wtforms.simplecodes.com>`_, by Thomas Johansson and James Crasta, is a forms library which is in appearance very close to Django's forms library, but is framework-agnostic.

WTForms is a great choice if you are using a lighter-weight framework with a standalone ORM. It integrates with result objects in a very elegant way.

Here's an example of a form taken straight from the docs. This is fairly similar to Django forms on the whole. As the forms are just python classes you can subclass forms quickly and easily to add an extra field if you need to.

.. sourcecode:: python

    from wtforms import Form, BooleanField, TextField, validators

    class ProfileForm(Form):
        """User profile."""
        birthday  = DateTimeField('Your Birthday', format='%m/%d/%y')
        signature = TextAreaField('Forum Signature')

Getting Data into the form
--------------------------

The really nice feature is how you can easily use both formdata and an object to update your form.

.. sourcecode:: python

    def edit_profile(request):
        user = request.current_user
        form = ProfileForm(request.POST, user)
        if request.method == 'POST' and form.validate():
            form.populate_obj(user)
            user.save()
            redirect('edit_profile')
        return render_response('edit_profile.html', form=form)

There's two things to note here. See the form instance is created by passing in the POST and the user object. Forms get data using the following precdences:

1. Form Data - form data has the highest priority
2. Data Object - the data object is the next in line. Usually an object returned by your ORM - e.g. Storm, SQLAlchemy
3. Kwargs - kwargs take the lowest priority.

So anything that's not present in the form data (e.g POST) is filled in by the data in the user object in our example above.

This means it's possible to make create/read/update and delete forms (CRUD) in an arbitrary way.

Updating DB objects with validated data
---------------------------------------

To update the db object ``form.populate_obj(obj)`` is used. This simply updates ``obj`` with the validated data based on matching it up to the object attrs. It's very neat and easy to use. With a bit of thought it's possible to use your favorite simple framework + your preferred ORM + WTForms and create a nice set of re-usable CRUD forms.

