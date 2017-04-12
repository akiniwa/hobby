# Example of handling attachments in Elasticsearch
# ================================================
#
# 1. Install the plugin: $ bin/elasticsearch-plugin install http://192.168.100.2:8000/ingest-attachment-5.1.1.zip
# 2. Run the script:     $ bash ingest_attachment.sh
#
# More info: <http://www.elasticsearch.org/guide/reference/mapping/attachment-type/>

echo '>>> delete index'
curl -X DELETE http://localhost:9200/ingest_attachment

echo;
echo '>>> create index'
curl -X POST http://localhost:9200/ingest_attachment -d '{
  "mappings" : {
    "document" : {
      "properties" : {
        "content" : {
          "type" : "attachment",
          "fields" : {
            "content"  : { "store" : "yes" },
            "author"   : { "store" : "yes" },
            "title"    : { "store" : "yes", "analyzer" : "smartcn"},
            "date"     : { "store" : "yes" },
            "keywords" : { "store" : "yes", "analyzer" : "smartcn" },
            "_name"    : { "store" : "yes" },
            "content_length" : { "store" : "yes" },
            "content_type" : { "store" : "yes" }
          }
        }
      }
    }
  }
}'

echo;
echo '>>> index the document'
curl -i -X PUT http://localhost:9200/ingest_attachment/document/1 -d "{
  \"_name\"    : \"test.docx\",
  \"content\"  : \"$(openssl base64 -in test.docx | tr -d '\n')\"
}"

echo;
echo '>>> refresh index'
curl -X POST http://localhost:9200/ingest_attachment/_refresh

echo;
echo ">>> search for '2016'"
curl "http://localhost:9200/ingest_attachment/_search?pretty=true&q=content:2016&stored_fields=*"
