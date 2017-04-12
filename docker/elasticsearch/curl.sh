curl -XGET 'http://dc:9200/library/docs/_search?pretty=1' -d '{
  "fields": [],
  "query": {
    "match": {
      "file.content": "社保"
    }
  },
  "highlight": {
    "fields": {
      "file.content": {
      }
    }
  }
}'