#! coding: utf-8
"""test.server.py"""

import webob
from paste import httpserver


def app(environ, start_response):
    """app"""
    request = webob.Request(environ)
    start_response("200 OK", [("Content-Type", "text/plain")])

    for name, value in request.POST.items():
        yield "%s: %s\n" % (name, value)

httpserver.serve(app, port=5000)
