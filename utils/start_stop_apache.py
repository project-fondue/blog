#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import socket

from optparse import OptionParser

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), "../"))
APACHE = "/usr/sbin/apache2"
APACHE_CONF_TEMPLATE = os.path.join(ROOT_DIR,
                                    "utils/templates/httpd.conf.template")
APACHE_CONF = "%s/tmp/httpd.conf" % ROOT_DIR

LOGDIR = '%s/tmp/logs' % ROOT_DIR
ERROR_LOG = "%s/apache.error_log" % LOGDIR
LOGFILE = "%s/apache.log" % LOGDIR
PIDFILE = '%s/tmp/apache.pid' % ROOT_DIR
PORTFILE = '%s/tmp/apache.port' % ROOT_DIR


VALID_CMDS = ["start", "stop"]


def get_unused_port():
    """Get unused port.

    http://code.activestate.com/recipes/531822-pick-unused-port/

    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    addr, port = s.getsockname()
    s.close()
    return port


def writeport(port_file, port):
    """Write the port number to disk."""
    fp = open(port_file, "w")
    fp.write(str(port))
    fp.close()


def writepid(pid_file):
    """Write the process ID to disk."""
    fp = open(pid_file, "w")
    fp.write(str(os.getpid()))
    fp.close()


def main():
    """run the command"""
    usage = "usage: %%prog %s [options]" % ("|".join(VALID_CMDS),)
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("Incorrect number of arguments")
    if args[0] not in VALID_CMDS:
        parser.error("Invalid action command")
    action = args[0]
    CMDS = {
        "start": start,
        "stop": stop,
    }
    CMDS[action]()


def start():
    """Run the server daemonized"""
    if os.path.exists(PORTFILE):
        port = open(PORTFILE, "r").read()
        print "We appear to already be serving the static content on "\
                        "http://localhost:%s" % (port,)
        return

    try:
        port = generate_apache_config()
    except:
        raise
        sys.exit(1)
    cmd = "%s -f %s -k start" % (APACHE, APACHE_CONF)
    print cmd
    os.system(cmd)
    print "Serving static content on http://localhost:%s" % port


def stop():
    """Kill the server"""

    cmd = "%s -f %s -k stop" % (APACHE, APACHE_CONF)
    os.system(cmd)

    if os.path.exists(PORTFILE):
        os.unlink(PORTFILE)


def generate_apache_config():
    """Generates the wsgi config from the template"""
    static_port_file = os.path.join(ROOT_DIR, "STATIC_APACHE_PORT")
    if os.path.exists(static_port_file):
        fh = open(static_port_file, "r")
        port = fh.read()
        fh.close()
    else:
        port = get_unused_port()
    writeport(PORTFILE, port)

    temp_vars = {}
    temp_vars["content_path"] = "%s/output/" % ROOT_DIR
    temp_vars["port"] = port
    temp_vars["pidfile"] = PIDFILE
    temp_vars["error_log"] = ERROR_LOG

    # open template
    tmp_file = open(APACHE_CONF_TEMPLATE, "r")
    template = tmp_file.read()

    tmp_file.close()

    template = template % temp_vars

    # open conf_file and write it out
    conf_file = open(APACHE_CONF, "w")
    conf_file.write(template)
    conf_file.close()

    return port

if __name__ == "__main__":
    main()
