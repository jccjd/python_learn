### web服务器和web框架

web服务器即是用来接受客户端请求，建立连接的程序， web框架则是用来处理业
务逻辑的，比如可以有很多的服务器`nginx`，`apche`，uWSGI也可以有很多的框
架，django，flask，那这些东西如何搭配就会有问题，那么这个问题的解决方就是
WSGI。 

所以WSGI 就如其名是一个网关接口，提供服务器和框架之间数据转发的一
个接口，要通过这个接口当然就需要一定的规范。下面就是这种规范的具体内容

### WSGI
在PEP 333 中的摘要给出，

> This document specifies a proposed standard interface between web servers and Python web applications or frameworks, to promote web application portability across a variety of web servers.

也就是说 WSGI 是指定Web服务器与Python Web应用程序或框架之间的标准接口，
以促进Web应用程序在各种Web服务器之间的可移植性。

而且由于早期的框架和服务器并不支持WSGI，而为了推广WSGI, WSGI 
就必须简单易于实现，使得框架作者的实现成本降低。


### django 中的WSGI

在django中的 wsgi.py 可以看到它是通过get_application()返回WSIGHandlers()
而在WSIGHandlers中实现了`__call__`使得其被调用时返回`response`，

**其中两个参数是必须的 `environ`, `start_response`**
    
    class WSGIHandler(base.BaseHandler):
        request_class = WSGIRequest
    
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.load_middleware()
    
        def __call__(self, environ, start_response):
            set_script_prefix(get_script_name(environ))
            signals.request_started.send(sender=self.__class__, environ=environ)
            request = self.request_class(environ)
            response = self.get_response(request)
    
            response._handler_class = self.__class__
    
            status = '%d %s' % (response.status_code, response.reason_phrase)
            response_headers = list(response.items())
            for c in response.cookies.values():
                response_headers.append(('Set-Cookie', c.output(header='')))
            start_response(status, response_headers)
            if getattr(response, 'file_to_stream', None) is not None and environ.get('wsgi.file_wrapper'):
                response = environ['wsgi.file_wrapper'](response.file_to_stream)
            return response
            
#### WSGI应用端   
application 端的协议就是这样的，这个api只需要两个参数，可以看到是非
常简单的，上面是框架中的东西，`PEP 333`,中给出了一个更简单的 事例，下面
对该事例进行了修改
    
    def simple_app(environ, start_response):
        stdout = "Hello world!"
        h = sorted(environ.items())
        for k,v in h:
            stdout += k + '=' + repr(v) + "\r\n"
        print(start_response)
        start_response("200 OK", [('Content-Type','text/plain; charset=utf-8')])
        return [stdout.encode("utf-8")]

上面的代码就算一个满足WSGI的Web应用程序，只要接收两个参数即可，看起来很
像是API，其实它的确可以是当作API来用的但是这是给框架开发者使用的，

> WSGI是面向框架、服务器开发者的工具，而不是为应用开发者直接提供支持的。

#### WSGI服务端

下面通过标准库中的`wsgiref.simple_server` 来实现一个简单的服务器，开启之
后即可，通过网页访问本地端口8000得到请求

    from wsgiref.simple_server import make_server

    httpd = make_server('', 8000, simple_app)
    print('Serving HTTP on port 8000...')
    httpd.serve_forever()


当从HTTP客户端收到一个请求，服务器就调用simple_app去做逻辑处理并返回处理
的结果集。
#### 中间件

中间件有着如下功能
- 在重写environ之后，相应地根据目标URL把请求发到对应的应用对象。
- 允许多个应用或者框架并行允许。
- 通过网络来转发请求和相应，实现负载均衡和远程处理。
- 对内容进行后续处理，比如应用XSL样式表

在web服务器和应用程序之间存在着中间件，在的django中存在的中间件去处理请求
视图，响应，模板，和异常，层层的包裹而形成了中间件栈(middleware stack)


        self._request_middleware = []
        self._view_middleware = []
        self._template_response_middleware = []
        self._response_middleware = []
        self._exception_middleware = []
那么这些中间件在出入栈的过程中，中间件的位置就成立相对位置，对服务器他是
应用，对于应用则他是服务.

### 参考

- [PEP 333 -- Python Web Server Gateway Interface v1.0](https://www.python.org/dev/peps/pep-0333/)
- [hongweipeng](http://www.hongweipeng.com/index.php/archives/1537/)
- [liaoxuefeng](https://www.liaoxuefeng.com/wiki/1016959663602400/1017805733037760)
