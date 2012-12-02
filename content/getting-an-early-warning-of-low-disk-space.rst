Getting an Early Warning of Low Disk Space
##########################################
:date: 2010-01-21 23:51
:category: blog
:tags: cron, linux, python, sysadmin, devops

Here's a really simple way of getting a notification when your disk space is running low by using a simple Python script in a cron job.

The idea is to configure a script with a threshold at which point if your free disk space is less that "n" percent you'll get an email telling you that you're running low on disk space.

Keeping an eye on Disk Space
============================

Running out of disk space is not a good situation to be in. Services that run out of disk space can cause your server to blow up in a very short space of time. As a result of that it's a good idea to get an early warning that your machine is on it's way to running out of disk space. This script is a noddy way to get that insight with minimum effort.

.. sourcecode:: python

    # -*- coding: utf-8 -*-

    """
    Disk Space
    Simple class for working out the free disk space on a system

    by Stuart Colville http://muffinresearch.co.uk 
    License: http://www.opensource.org/licenses/mit-license.php

    """

    import os
    import math

    class DiskSpace():
        
        """Free Disk Space"""
        
        def __init__(self, path="/"):
            """Init class and retrieves disk space info"""
            self.disk = os.statvfs(path)

        def has_free_space(self, limit):
            """Bool returns true if remaining space is above limit %"""
            if float(self.percent_free()) < float(limit):
                return False
            else:
                return True

        def percent_free(self):
            """Gets the amount of space left as a percentage"""
            return (math.ceil(float(100) / float(self.bytes_capacity()) 
                                                    * self.bytes_free()))

        def bytes_capacity(self):
            """Returns the total capacity in bytes"""
            return self.disk.f_frsize * self.disk.f_blocks
            
        def bytes_free(self):
            """Returns the free space in bytes"""
            return self.disk.f_frsize * self.disk.f_bavail
           
        def bytes_used(self):
            """Returns the used space in bytes"""
            return self.disk.f_frsize * (self.disk.f_blocks - 
                                                       self.disk.f_bavail)
                
        @staticmethod
        def humanize_bytes(bytes, kilo=1024):
            
            """Humanizes bytes
             
            See http://en.wikipedia.org/wiki/Kilobyte for info on the 
            different ways to interpret whether a kilobyte is 1,024 bytes 
            or 1,000 bytes
            
            """
            
            if kilo == 1024:
                label = ["KiB", "MiB" , "GiB", "TiB"]
            else:
                # fallback
                kilo = 1000
                label = ["KB", "MB" , "GB", "TB"]    

            if bytes < kilo:
                return "%d" % bytes
            elif bytes > kilo and bytes < math.pow(kilo, 2):
                return "%.2F%s" % (float(bytes/kilo), label[0])
            elif bytes > math.pow(kilo, 2) and bytes < math.pow(kilo, 3):
                return "%.2F%s" % (float(bytes/math.pow(kilo, 2)), label[1])
            elif bytes > math.pow(kilo, 3) and bytes < math.pow(kilo, 4):
                return "%.2F%s" % (float(bytes/math.pow(kilo, 3)), label[2])
            elif bytes > math.pow(kilo, 4) and bytes < math.pow(kilo, 5):
                return "%.2F%s" % (float(bytes/math.pow(kilo, 4)), label[3])
                

Example
=======

Here's a quick example of how this can be used in practice

.. sourcecode:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    """Simple example command line usage:

    Usage: ./check_disk_space.py <percentage free space>

    e.g:

    $ ./check_disk_space.py 30
    Running low on disk space. 20.0% remaining (Warning Threshold: 30%)
    Total: 115.13GB
    Used:  92.35GB
    Avail: 22.77GB

    The idea would be to put this in a Cron Job and have it email you when 
    the free disk space is lower than "n" percent.

    """

    import sys

    sys.path.insert(0, '../')

    from diskspace import DiskSpace

    ds = DiskSpace()

    perc_arg = len(sys.argv) > 1 and sys.argv[1] or None
    percent_limit = perc_arg or 20

    if not ds.has_free_space(percent_limit):
        print "Running low on disk space. %s%% remaining "\
           "(Warning Threshold: %s%%)" % (ds.percent_free(), percent_limit) 
        print "Total: %s" % ds.humanize_bytes(ds.bytes_capacity(), 1000)
        print "Used:  %s" % ds.humanize_bytes(ds.bytes_used(), 1000)
        print "Avail: %s" % ds.humanize_bytes(ds.bytes_free(), 1000)

This last file can be saved as check_disk_space.py and made executable with:

.. sourcecode:: sh

    chmod +x check_disk_space.py

All you then need to do is add a crontab entry and define the limit at which you want to be warned of impending disk space running out.

.. sourcecode:: cron

    MAILTO=systems@yourdomain.com
    0 */2 * * * /path/to/file/free_disk_space 15


This example will check the space every 2 hours and will email you when the remaining disk space drops below 15%.

A Branch of these files is available here: http://code.projectfondue.com/diskspace/trunk/files/head:/diskspace/

Suggestions for improvement are always welcome.

