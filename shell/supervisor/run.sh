./config.supervisord.sh "elasticsearch" "elasticsearch" "/opt/elasticsearch" "elasticsearch"; \
./config.supervisord.sh "logstash"      "logstash"      "/opt/logstash"      "elasticsearch"; \
./config.supervisord.sh "kibana"        "kibana"        "/opt/kibana"        "elasticsearch"
