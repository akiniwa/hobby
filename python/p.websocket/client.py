#! coding: utf-8

import base64
# from websocket import create_connection


# def send_msg(msg):
#     """send_msg"""
#     ws = create_connection("ws://localhost:8181/")
#     print "client> {}".format(msg)
#     ws.send(msg)
#     print "server< {}".format(ws.recv())
#     ws.close()

# send_msg('hello world')
print(base64.urlsafe_b64encode('b+EMfwNSGHQ3sBjqvEMlf8FP1Lc='))
print(base64.b64decode('zsZES2A/XDzGAHOfXAp3LzUgU8s='))
print(base64.b64encode('this is a string'), 'aa')
