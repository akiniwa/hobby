#! coding: utf-8
"""test.client.py"""

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import poster
import cookielib

UPLOAD_URL = 'http://localhost:5000/upload'


def demo1():
    """demo1"""
    # Register the streaming http handlers with urllib2
    register_openers()

    # Start the multipart/form-data encoding of the file "test.client.py"
    # "file" is the name of the parameter, which is normally set
    # via the "name" parameter of the HTML <input> tag.

    # headers contains the necessary Content-Type and Content-Length
    # datagen is a generator object that yields the encoded parameters
    datagen, headers = multipart_encode({"file": open("test.client.py", "rb")})

    # Create the Request object
    request = urllib2.Request(UPLOAD_URL, datagen, headers)
    # Actually do the request, and get the response
    print headers
    print urllib2.urlopen(request).read()


def demo2():
    """demo2"""
    opener = poster.streaminghttp.register_openers()
    opener.add_handler(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

    params = {'file': open("test.client.py", "rb"), 'name': 'upload test'}
    datagen, headers = poster.encode.multipart_encode(params)
    request = urllib2.Request(UPLOAD_URL, datagen, headers)
    print headers
    print urllib2.urlopen(request).read()

demo1()
demo2()
