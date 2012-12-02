CSS Sprite Generator v4.0 available on Launchpad
################################################
:date: 2009-09-01 11:03
:tags: css, performance, sprites
:category: blog


We've recently released the source code for version 4 of our CSS sprite generator. 

We've done a fair amount of restructuring, fixed a few bugs and added an important new feature - the ability to generate sprites with their component images stacked in horizontal or vertical orientation. 


This is useful for sprites which contain gradients that need to be repeated in a specific direction. There's also been some suggestion, particularly from the Yahoo! performance guys, that `building sprites horizontally results in a smaller overall image size <http://developer.yahoo.com/performance/rules.html#opt_sprites>`_.
        
    Arranging the images in the sprite horizontally as opposed to vertically usually results in a smaller file size.
        
    -- Yahoo! Exceptional Performance Team
        
Other Changes
=============
        
Generated CSS
-------------
        
Displaying the generated CSS within a textarea field (rather than a scrolling div) to enable select all and easier copy and paste.
        
Component Spacing
-----------------
        
A reduction in the default spacing (horizontal and vertical) between component images in the sprite. This makes the tool kinder to our servers and means, with a default generation, the browser has to handle a smaller uncompressed image in memory. `This should be of particular benefit to the iphone which doesn't seem to handle large sprites too well. <http://developer.yahoo.com/performance/rules.html#opt_sprites>`_
        
    "Be mobile-friendly" and don't leave big gaps between the images in a sprite. This doesn't affect the file size as much but requires less memory for the user agent to decompress the image into a pixel map. 100x100 image is 10 thousand pixels, where 1000x1000 is 1 million pixels
        
    -- Yahoo! Exceptional Performance Team
        
There's a balance to be had here, of course. The usual reason for including space between component images is to allow for text sizes increases which would otherwise result in partial display of the next image in the sprite. You can see how this would be a particular problem on something like the navigation of the `Yahoo! home page <http://www.yahoo.com/>`_.
        
Language Selection
------------------
        
Conversion of the language selection interface from a drop down box to a list of links to make it easier for someone to switch to their native language, particularly where they don't understand the currently displayed language. There's an `interesting analysis of the use of drop downs versus links <http://www.w3.org/International/questions/qa-navigation-select>`_ in the W3C i18n FAQ with the relative benefits and pitfalls of each approach.
        
Looking Forward
===============
        
We've got a few other bugs that need fixing. We'll be working on those shortly and, in due course, we'll also be developing a command line version of the tool. This should make it easy to incorporate into an automated build script. Check back regularly for further details and do drop us a line if you've got any suggestions.

Get the Code
============

You can `get the source code here on Launchpad <https://launchpad.net/css-sprite-generator>`_. As always comments, suggestions, bugs and patches are welcomed.

Try Version 4 Online
=====================

`CSS Sprite Generator version 4 <http://spritegen.website-performance.org/>`_ is available online where you can dive right in and try out the latest features. 
