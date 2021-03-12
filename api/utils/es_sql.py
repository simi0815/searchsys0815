from elasticsearch import Elasticsearch


class ElasticObj:
    def __init__(self, index_name,ip ="https:/192.168.1.230"):
        '''

        :param index_name: 索引名称
        :param index_type: 索引类型
        '''
        self.index_name =index_name
        # 无用户名密码状态
        #self.es = Elasticsearch([ip])
        #用户名密码状态
        self.es = Elasticsearch([ip],http_auth=('elastic', 'twdtwd'),port=9200)

    def Get_Data_By_Body(self):
        # doc = {'query': {'match_all': {}}}
        doc = {
            "query": {
                "match": {
                    # "first_name": "ds"
                }
            }
        }
        _searched = self.es.search(index=self.index_name, body=doc)

        for hit in _searched['hits']['hits']:
            # print hit['_source']
            print (hit['_source']['date'], hit['_source']['source'], hit['_source']['link'], hit['_source']['keyword'],
            hit['_source']['title'])




obj =ElasticObj("person_apollo")
obj.Get_Data_By_Body()
# obj = ElasticObj("ott1", "ott_type1")

# obj.create_index()

# obj.bulk_Index_Data()
# obj.IndexData()
# obj.Delete_Index_Data(1)
# csvfile = 'D:/work/ElasticSearch/exportExcels/2017-08-31_info.csv'
# obj.Index_Data_FromCSV(csvfile)
# obj.GetData(es)