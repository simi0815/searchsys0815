from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['192.168.1.230:9200'],
    http_auth=('elastic', 'twdtwd'),
    use_ssl=True,
    verify_certs=False,
)


dsl = {
    "query":{
        "match_all":{}
    }
}
index_name = 'person_apollo'
res = es.search(index=index_name, body=dsl)
print(res)