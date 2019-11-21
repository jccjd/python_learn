from wsgiref.simple_server import WSGIServer, WSGIRequestHandler


def demo_app(environ, start_response):
    """
    示例的 app
    """
    stdout = "Hello world!"
    h = sorted(environ.items())
    for k, v in h:
        stdout += k + '=' + repr(v) + "\r\n"
    print(start_response)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return [stdout.encode("utf-8")]


class StaticFilesHandler:
    """
    处理静态文件的句柄
    """

    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        if True:  # 假设所有请求都不是静态文件
            return self.application(environ, start_response)


class HttpRequest(object):
    """
    定义request所需的属性
    """

    def __init__(self):
        self.GET = {}
        self.POST = {}
        self.COOKIES = {}
        self.META = {}
        self.FILES = {}

        self.path = ''
        self.path_info = ''
        self.method = None


class WSGIRequest(HttpRequest):
    """
    将环境变量转到 request 属性
    """

    def __init__(self, environ):
        super(WSGIRequest, self).__init__()
        script_name = environ["SCRIPT_NAME"]
        path_info = environ["PATH_INFO"]
        if not path_info:
            path_info = '/'
        self.environ = environ
        self.path_info = path_info

        self.path = '%s/%s' % (script_name.rstrip('/'), path_info.replace('/', '', 1))
        self.META = environ
        self.META['PATH_INFO'] = path_info
        self.META['SCRIPT_NAME'] = script_name
        self.method = environ['REQUEST_METHOD'].upper()


class HttpResponse(object):
    """
    一个简单封装的response类
    """

    def __init__(self, content="", status=200,
                 charset="utf-8", content_type="text/plain; charset=utf-8",
                 *args, **kwargs):
        self._headers = {'Content-Type': content_type}
        self._charset = charset
        self.content(content)
        self.status_code = status

    def serialize_headers(self):
        def to_bytes(val, encoding):
            return val if isinstance(val, bytes) else val.encode(encoding)

        headers = [
            (b': '.join([to_bytes(key, 'ascii'), to_bytes(value, 'latin-1')]))
            for key, value in self._headers.values()
        ]
        return b'\r\n'.join(headers)

    def content(self, value):  # 将str转换为 [bytes()] 形式
        content = bytes(value.encode(self._charset))
        self._container = [content]

    def __iter__(self):
        return iter(self._container)


def get_response(request):
    """
    示例
    :param request:
    :return:
    """
    print("path = %s" % request.path)
    print("method = %s" % request.method)
    res = HttpResponse("hello world")
    res.status_code = 200
    res._headers["hahahah"] = "xxxxxx"
    return res


class WSGIHandler(object):
    """
    WSGI句柄, 起中心调控作用
    """
    request_class = WSGIRequest

    def __call__(self, environ, start_response):
        request = self.request_class(environ)
        response = get_response(request)
        status = '%d %s' % (response.status_code, "OK")
        response_headers = [(str(k), str(v)) for k, v in response._headers.items()]
        start_response(str(status), response_headers)
        return response


server = WSGIServer(('', 8000), WSGIRequestHandler)
application = WSGIHandler()
static_handler = StaticFilesHandler(application)
server.set_app(static_handler)
server.serve_forever()
