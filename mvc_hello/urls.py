from handlers.index import IndexHandler, HomeHandler

urls = [
    (r'/', IndexHandler),
    (r'/home', HomeHandler)

]