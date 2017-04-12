
echo 'delete index'
curl -XDELETE 'http://node2:9200/library'
echo '-------------------------------------------';

echo 'create index'
curl -XPUT    'http://node2:9200/library' -d '{
    "settings" : {
        "index" : {
            "number_of_shards" : 1, 
            "number_of_replicas" : 0
        }
    }
}'
echo '-------------------------------------------';

echo 'create mapping'
curl -XPUT 'http://node2:9200/library/docs/_mapping?pretty=1' -d '{
    "properties" : {
        "file" : {
            "type" : "attachment",
            "fields" : {
                "content": {
                    "type": "string",
                    "term_vector": "with_positions_offsets",
                    "store": true
                },
                "content_type": {"type": "string", "store": "yes"},
                "name": {"type": "string", "store": "yes"},
                "title": {"store": "yes"},
                "content_length": {"store": "yes"}
            }
        }
    }
}'
echo '-------------------------------------------';

echo 'refresh index'
curl -XPOST 'http://node2:9200/library/_refresh?pretty=1'
echo '-------------------------------------------';


echo 'indexed test.doc';
curl -XPOST "http://node2:9200/library/docs?pretty=1" -d @- '
{
    "file" : {
        "content_type": "doc",
        "_content" : "'`base64 data/test.doc | perl -pe 's/\n/\\n/g'`'"
    }
}'
echo '-------------------------------------------';

echo 'indexed test.pdf';
curl -XPOST "http://node2:9200/library/docs?pretty=1" -d '
{
    "file" : {
        "content_type": "pdf",
        "_content" : "'`base64 data/test.pdf | perl -pe 's/\n/\\n/g'`'"
    }
}'
echo '-------------------------------------------';

echo 'indexed test.ppt';
curl -XPOST "http://node2:9200/library/docs?pretty=1" -d '
{
    "file" : {
        "content_type": "ppt",
        "_content" : "'`base64 data/test.ppt | perl -pe 's/\n/\\n/g'`'"
    }
}'
echo '-------------------------------------------';

echo 'indexed test.xls';
curl -XPOST "http://node2:9200/library/docs?pretty=1" -d '
{
    "file" : {
        "content_type": "xls",
        "_content" : "'`base64 data/test.xls | perl -pe 's/\n/\\n/g'`'"
    }
}'
echo '-------------------------------------------';

curl -XGET 'http://node2:9200/library/docs/_search?pretty=1' -d '{
  "fields": [],
  "query": {
    "match": {
      "file.content": "地税"
    }
  },
  "highlight": {
    "fields": {
      "file.content": {
      }
    }
  }
}'

curl -XGET 'http://node2:9200/library/docs/_search?pretty=1' -d '{
  "fields": [],
  "query": {
    "match": {
      "file.content": "海关"
    }
  },
  "highlight": {
    "fields": {
      "file.content": {
      }
    }
  }
}'

curl -XGET 'http://node2:9200/library/docs/_search?pretty=1' -d '{
  "fields": [],
  "query": {
    "match": {
      "file.content": "公积金"
    }
  },
  "highlight": {
    "fields": {
      "file.content": {
      }
    }
  }
}'

curl -XGET 'http://node2:9200/library/docs/_search?pretty=1' -d '{
  "fields": [],
  "query": {
    "match": {
      "file.content": "社会保险"
    }
  },
  "highlight": {
    "fields": {
      "file.content": {
      }
    }
  }
}'
