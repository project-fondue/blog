Google Chrome Frame — good or bad for the web?
##############################################
:date: 2009-10-02 20:35
:category: blog
:tags: accessibility, browsers, google

Google Chrome Frame is a plugin released by Google designed to provide the Google Chrome Browser engine inside of a frame in IE 6,7 and 8.

Here is Google's description of what Chrome Frame is:

    Google Chrome Frame is an early-stage open source plug-in that seamlessly brings Google Chrome's open web technologies and speedy JavaScript engine to Internet Explorer. With Google Chrome Frame, you can:

    * Start using open web technologies - like the HTML5 canvas tag - right away, even technologies that aren't yet supported in Internet Explorer 6, 7, or 8.
    * Take advantage of JavaScript performance improvements to make your apps faster and more responsive.

    -- http://code.google.com/chrome/chromeframe/

I'm intrigued by `Google Frame <http://code.google.com/chrome/chromeframe/>`_; on one hand it's a pretty neat way of providing a more advanced experience to users of Internet Explorer, but I'm also concerned that it's providing a prop to browsers that really should be moving towards deprecation. If a browser isn't capable of displaying a site wouldn't it make more sense to point people in the direction of browsers that are more advanced?

Is this also saying that Google Wave will need Chrome Frame because it will only be meaningful to users with the most up to date technology. If you aren't up to date is there no base-line experience? If that's the case, a future that ignores progressive enhancement has a nasty aroma to it.

.. admonition:: Update: 24th September 2009

    `According to this post on the Google Wave Blog <http://googlewavedev.blogspot.com/2009/09/google-wave-in-internet-explorer.html>`_, it seems IE 6,7 and 8 users will not be able to use Google Wave unless they install the Google Frame Plugin.

Google Frame and Accessibility
==============================

`Early investigations by Steve Faulkner <http://www.paciellogroup.com/blog/?p=444>`_ have shown that the inclusion of Google Frame locks out users of assisitive technologies completely. 

Clearly this is an early release and assistive technology support could be improved in a future release. Whilst I'm happy to be proved wrong, I somehow doubt this will change given the epic technical challenges involved. That said, if anyone can do it, Google is a company that is best placed to make it happen.

Elsewhere
---------

* `A Microsoft Spokesperson says Google Chrome Frame makes IE less secure <http://arstechnica.com/microsoft/news/2009/09/microsoft-google-chrome-frame-makes-ie-less-secure.ars>`_
* `More technical details about Google Chrome Frame <http://jimray.tumblr.com/post/194793633/more-technical-details-about-google-chrome-frame>`_
* `Google Groups thread with further comment on the acessibility issues <http://groups.google.com/group/google-chrome-frame/browse_thread/thread/7d94aff736a42d29/b3f63eb21c983fd9?hl=en&#b3f63eb21c983fd9>`_


