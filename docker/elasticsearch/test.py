#! encoding: utf-8
import base64
import os
import json
from elasticsearch import Elasticsearch
# es = Elasticsearch(host='dc', port='9200')
es = Elasticsearch(host='node2', port='9200')

library = 'library'


def print_result(result):
    """print_result"""
    print(json.dumps(result, indent=4))


def create():
    """create index"""
    body = {
        "mappings": {
            "docs": {
                "properties": {
                    "file": {
                        "type": "attachment",
                        "fields": {
                            "content": {
                                "type": "string",
                                "term_vector": "with_positions_offsets",
                                "store": True
                            },
                            "content_type": {"type": "string", "store": "yes"},
                            "name": {"type": "string", "store": "yes"},
                            "title": {"store": "yes"},
                            # "date": {"store": "yes"},
                            # "author": {"analyzer": "myAnalyzer"},
                            # "keywords": {"store": "yes"},
                            "content_length": {"store": "yes"},
                            # "language": {"store": "yes"}
                        }
                    }
                }
            }
        }
    }
    # ignore 400 cause by IndexAlreadyExistsException when creating an index
    result = es.indices.create(index=library, body=body, ignore=400)
    print_result(result)


def delete():
    """delete index"""
    # ignore 404 and 400
    result = es.indices.delete(index=library, ignore=[400, 404])
    print_result(result)


def encode():
    """encode"""
    files = ['test.xls', 'test.pdf', 'test.ppt', 'test.doc']
    for file in files:
        file_n = os.path.join('data', file)
        with open(file_n, 'rb') as f:
            base = base64.b64encode(f.read())
            content = base.decode('ascii')
            print base
            print content
            break


def index():
    files = ['test.xls', 'test.pdf', 'test.ppt', 'test.doc']
    for file in files:
        file_n = os.path.join('data', file)
        with open(file_n, 'rb') as f:
            content = base64.b64encode(f.read()).decode('ascii')
            # print content
            result = es.index(
                index=library,
                doc_type='docs',
                pipeline='attachment',
                body={
                    'content_type': file.split('.')[1],
                    'content': content,
                    'name': file_n,
                },
                refresh=True)
            print('index file {}'.format(file_n))
            print_result(result)


def refresh():
    """refresh index"""
    result = es.indices.refresh(index=library, force=True)
    print_result(result)


def search(q):
    """"""
    body = {
        # "fields": [],
        "fields": ["name", "content"],
        "query": {
            "match": {
                "file.content": q
            }
        },
        "highlight": {
            "fields": {
                "file.content": {}
            }
        }
    }
    result = es.search(
        index=library,
        doc_type='docs',
        body=body
    )
    # print(u'search {}'.format(q))
    print """<!DOCTYPE html>
        <head>
        <style type="text/css">
        em {
            color: red;
        }
        </style>
        </head>
        <body>"""
    # print_result(result)
    for hit in result['hits']['hits']:
        ctt = hit['highlight']['file.content'][0].replace('\n', '')
        print u'<p>{}</p>'.format(ctt)
    print "</body>"


if __name__ == '__main__':
    delete()
    create()
    index()
    refresh()
    search(u'地税')
    # search(u'海关')
    # search(u'公积金异地')
    # search(u'社会保险')

    # encode()
