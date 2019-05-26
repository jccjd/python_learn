import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("hello")

class HomeHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.write("home")
