#! coding: utf-8

from websocket import create_connection


def send_msg(msg):
    """send_msg"""
    ws = create_connection("ws://localhost:8181/")
    print "client> {}".format(msg)
    ws.send(msg)
    print "server< {}".format(ws.recv())
    ws.close()

send_msg('hello world')
