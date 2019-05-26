#coding:utf-8
#author:the5fire

import os

import tornado.web
import config
from urls import urls
from handlers.index import IndexHandler, HomeHandler


# class Application(tornado.web.Application):
#     def __init__(self):
#         handlers = [
#             (r'/',IndexHandler),
#             (r'/home',HomeHandler),
#         ]
#
#         super(Application,self).__init__(handlers,**config.settings)

SETTINGS = dict(
template_path=os.path.join(os.path.dirname(__file__), "templates"),
static_path=os.path.join(os.getcwd(), "static"), ##合并路径
##static_path=os.path.join(os.path.dirname(__file__), "static"),
##os.getcwd() 他返回的路劲是根目录及E:\Orgappserver
# 由于os.path.join()的作用是拼接路劲所以sing出来的结果E:\\Orgserverapppc\\static
)

webapplication = tornado.web.Application(
                handlers=urls,
                **SETTINGS
)