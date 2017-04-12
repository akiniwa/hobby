from elasticsearch import Elasticsearch

es = Elasticsearch()
print es.cat.health()

body = {
	"description" : "Extract attachment information",
	"processors" : [
		{
		"attachment" : {
		"field" : "data"
		}
		}
	]
}
es.index(index='_ingest', doc_type='pipeline', id='attachment', body=body)

result1 = es.index(index='my_index', doc_type='my_type', pipeline='attachment',
                  body={'data': "e1xydGYxXGFuc2kNCkxvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0DQpccGFyIH0="})
result1