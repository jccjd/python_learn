#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import tornado.httpserver
import tornado.ioloop

from tornado.options import options, define
from application import webapplication



define("port", default=9000, help="run on the given port", type=int)


def main():
    print ("run on the given port: %d" % options.port)
    print "Quit the server with CONTROL-C "
    http_server = tornado.httpserver.HTTPServer(webapplication)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
