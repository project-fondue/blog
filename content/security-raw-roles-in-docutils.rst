Security: Raw Roles in Docutils
###############################
:date: 2010-07-27 22:23
:tags: restructuredtext, security
:category: blog

Whilst we were making our reStructuredText API site, we found a flaw in docutils 0.5 which made it possible to inject arbitrary html and javascript into any website or wiki which allows third parties to provide content via restructured text.

The flaw occurs via the roles feature which is designed to allow the author to bypass the parsing of rst. The only problem was that despite the options being set to disable the raw directive which similarly allows unfiltered text, the raw role was still permitted.


Here's an example of how this could be used:

.. sourcecode:: rst

    .. role:: unsafe_raw(raw)
        :format: html

    :unsafe_raw:`<p onclick="alert('hello')">Oh Hai (click me)</p>`

The good news is following the provision of a `patch <http://sourceforge.net/tracker/?func=detail&atid=422030&aid=2845002&group_id=38414>`_ this was fixed in release 0.6 of docutils. If you're using reStructuredText on your site where third parties can use it to provide content, it's definitely recommended that you check to make sure you're using 0.6 or higher.

Related Reading
---------------

* `The documentation for the raw role <http://docutils.sourceforge.net/docs/ref/rst/roles.html#raw>`_
* `The related bug on sourceforge <http://sourceforge.net/tracker/?func=detail&atid=422030&aid=2845002&group_id=38414>`_ 
* `Our reStructuredText API <http://rst.projectfondue.com>`_

