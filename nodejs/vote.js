var redis = require("redis");
var client = redis.createClient();
client.set("article:100:headline", "hqlgree2's book one");
client.set("article:135:headline", "hqlgree2's book two");

function upVote(id){
    var key = "article:" + id + ":votes";
    client.incr(key);
}

function downVote(id){
    var key = "article:" + id + ":votes";
    client.decr(key);
}

function showResults(id){
    var headlineKey = "article:" + id + ":headline";
    var voteKey = "article:" + id + ":votes";
    client.mget([headlineKey, voteKey], function(err, replies){
        console.log('the article "' + replies[0] + '" has', replies[1], 'votes');
    });
}

upVote(100);
upVote(100);
upVote(100);
upVote(135);
upVote(135);
downVote(135);

showResults(100);
showResults(135);

client.quit();
