# ws://logbook.jd.com/socket.io/?EIO=3&transport=websocket&sid=PKE0TPmh0J08ssn2AAAS

import websocket, httplib

# ...

# '''
#     connect to the socketio server

#     1. perform the HTTP handshake
#     2. open a websocket connection '''
# def connect(self) :
#     conn  = httplib.HTTPConnection('localhost:8124')
#     conn.request('POST','/socket.io/1/')
#     resp  = conn.getresponse() 
#     hskey = resp.read().split(':')[0]

# def onopen():
#   print 'open'

# def onmessage(msg):
#   print msg

# ws = websocket.WebSocket(
#     'ws://logbook.jd.com/socket.io/?EIO=3&transport=websocket&sid=PKE0TPmh0J08ssn2AAAS',
#     onopen   = onopen,
#     onmessage = onmessage)

# ws.run_forever()

# from socketIO_client import SocketIO


# socketIO = SocketIO('192.168.43.245', 3000, Fruitspace)
# fruitSocket = socketIO.define(Fruitspace, '/box')
# print("Wait for Connect..")
# fruitSocket.on('heartbeat', on_mainHeartbeat)
# fruitSocket.emit('heartbeat', {})
# socketIO.wait()

import websocket
import thread
import time

def on_message(ws, message):
    print message

def on_error(ws, error):
    print 'websocket error', error

def on_close(ws):
    print 'websocket close'

def on_open(ws):
    print 'websocket open'

data_ws = 'ws://logbook.jd.com/socket.io/?EIO=3&transport=websocket&sid=msK615OoxQVwuOlbAAAY'
data_ck = 'io=msK615OoxQVwuOlbAAAY; TrackID=1ZuvgVKiamJM3NtEn2vQFt2mied02pUd2y6M0E4gX5C_DATHsscY-RmFbyi2bi0JmaNv120mkNX1i89ZNGh_2rw; pinId=YmDIwhhdAJK1ffsfn98I-w; user-key=8e667beb-3912-48aa-9052-20ee1fe93d7f; cn=0; ipLoc-djd=1-72-2799-0; ipLocation=%u5317%u4EAC; __jdv=122992088|direct|-|none|-; logbook_u=houqiangliang; logbook_k=feb72f117b; erp1.jd.com=DF2E6D1B5A99F51F7BAB754C7A683B57FABA14DD684D8F0941E16EBD1B2969600FF13DF752EC5C9E5FFCDF64C00BE6960858AF0CE6A709EC0901B7F7472A096BAD84FDA58D34C01052C340B8E14D29F0AD9BBD1464EB8E8035803B10ABEF29FA; sso.jd.com=27c3c2d3dd1f49d9b83784db5634382a; __jda=137720036.1842287236.1469147786.1473843417.1474263743.14; __jdc=137720036; __jdu=1842287236; 3AB9D23F7A4B3C9B=265696505cf14ead8c7c44dbb4aee3372048680323'


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        data_ws,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        cookie=data_ck)
    ws.on_open = on_open
    ws.run_forever()