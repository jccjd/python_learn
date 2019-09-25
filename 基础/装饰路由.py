# -*- coding: utf-8 -*-
import re


class NotFlask():
    def __init__(self):
        self.routes = []

    @staticmethod
    def build_route_pattern(route):

        route_regex = re.sub(r'(<.*?>)', r'(?P\1.+)', route)
        return re.compile('^{}$'.format(route_regex))

    def route(self, route_str):
        def decorator(func):
            route_pattern = self.build_route_pattern(route_str)
            self.routes.append((route_pattern, func))

            return func

        return decorator

    def get_route_match(self, path):
        for route_pattern, view_function in self.routes:
            m = route_pattern.match(path)
            if m:
                return m.groupdict(), view_function
        return None

    def save(self, path):
        route_match = self.get_route_match(path)

        if route_match:

            kwargs, view_function = route_match

            return view_function(**kwargs)
        else:
            raise ValueError('Route has not found')


app = NotFlask()


@app.route("/hell/<username>")
def hell(username):
    return 'jj{}'.format(username)

@app.route("/hello/dd/<username>")
def hello(username):

    return username


print(app.save("/hell/admin"))
print(app.save("/hello/dd/admin"))


