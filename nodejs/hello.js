var redis = require("redis");
var client = redis.createClient();
client.set("gree2", "hqlgree2 from node.js");
client.get("gree2", redis.print);
client.quit();
