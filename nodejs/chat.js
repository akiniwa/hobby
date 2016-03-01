var uuid = require('node-uuid');
var WebSocketServer = require('ws').Server,
    ws = new WebSocketServer({port: 8181});

var clients = [];

function wsSend(type, client_uuid, nickname, message) {
    for (var i=0; i<clients.length; i++) {
        var clientSocket = clients[i].ws;
        if (clientSocket.readyState === WebSocket.OPEN) {
            clientSocket.send(JSON.stringify({
                "type": type,
                "id": client_uuid,
                "nickname": nickname,
                "message": message
            }));
        }
    }
}

var clientIndex = 1;

ws.on('connection', function(ws) {
    var client_uuid = uuid.v4();
    var nickname = "anonymous_user_" + clientIndex;
    clientIndex += 1;
    client.push({"id": client_uuid, "ws": ws, "nickname": nickname});
    console.log('client [%s] connected', client_uuid);
    var connect_message = nickname + " has connected";
    wsSend("message", client_uuid, nickname, message);

    ws.on('message', function(message) {
        if(message.indexOf('/nick') === 0) {
            var nickname_array = message.split(' ');
            if (nickname_array.length >= 2) {
                var old_nickname = nickname;
                nickname = nickname_array[1];
                var nickname_message = "client " + old_nickname + " changed to " + nickname;
                wsSend("nick_update", client_uuid, nickname, nickname_message);
            }
        } else {
            wsSend("message", client_uuid, nickname, message);
        }

    });

    var closeSocket = function(customMessage) {
        for(var i=0; i<clients.length; i++) {
            if (clients[i].id == client_uuid) {
                var disconnected_message;
                if (customMessage) {
                    disconnected_message = customMessage;
                } else {
                    disconnected_message = nickname + "has disconnected";
                }
                wsSend("notification", client_uuid, nickname, disconnected_message);
                clients.splice(i, 1);
            }
        }
    }

    ws.on('close', function() {
        closeSocket();
    });

    process.on('SIGINT', function() {
        console.log("closing things");
        closeSocket("server has disconnected");
        process.exit();
    });
});