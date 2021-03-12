# from pymongo import MongoClient
#
# MONGO_ADDRESS = '192.168.1.231'
# MONGO_PORT = 27017
#
#
# # class Database(object):
# #     def __init__(self, address=MONGO_ADDRESS, port=MONGO_PORT):
# #         self.conn = MongoClient(host=address, port=port, serverSelectionTimeoutMS=3000000)
# #         self.db = self.conn["lingying-db"]
# #         res = self.db["pdl-coll"].find({'name': {'$regex':'kos'}})
# #         print(list(res))
# # d = Database()
# l = ['a','b']
# for index in range(len(l)):
#    print ('当前水果 :', l[index])

res =  [
            {
                "_id": "5a8fdb712467a7bb10fedf74",
                "email": "tom.mahoney@hotmail.com",
                "company_name": "Public Art Fund Inc",
                "title": "President",
                "linkedin account": "tom.mahoney",
                "city": "sumner",
                "state": "wa",
                "zip": 98391,
                "fax": 2539055623,
                "company_website": "publicartfund.org",
                "email_lower_sha256": "535a73a2d49a73183f674c84d2c70c99ee0b4a98030ca9d857e57c9106777c8e",
                "addr_01": "8804 186th ave e",
                "first_name": "tom",
                "last_name": "mahoney",
                "tel": "",
                "i_col": "businessleads",
                "i_db": "verifications-db",
                "db_type": "mongo",
                "name": "tom mahoney"
            },
            {
                "_id": "5a8fdb712467a7bb10fef6fe",
                "email": "tom.mahoney@hotmail.com",
                "company_name": "james c. gallo",
                "title": "Manager",
                "linkedin account": "leonard.tom",
                "city": "st peter",
                "state": "mn",
                "zip": 56082,
                "fax": 5073852500,
                "company_website": "domesticbattery.com",
                "email_lower_sha256": "8c92e4cdd8c60b339b649c58ccf8043bf80dbd22121b6d429e3e9f4a031c337a",
                "addr_01": "311 wabasha",
                "first_name": "tom",
                "last_name": "leonard",
                "tel": "",
                "i_col": "businessleads",
                "i_db": "verifications-db",
                "db_type": "mongo",
                "name": "tom leonard"
            },
            {
                "_id": "5a8fdb712467a7bb10ff1881",
                "email": "tmarcy@yahoo.com",
                "company_name": "Ymca",
                "title": "Executive Director",
                "linkedin account": "tmarcy",
                "city": "kansas city",
                "state": "mo",
                "zip": 64154,
                "fax": 8168108899,
                "company_website": "chemungymca.org",
                "email_lower_sha256": "8cba87b3d76d1792a018f2a7898f26d5200c0dfe7e0ec939e6aa12e19b3752f0",
                "addr_01": "3933 nw 85th ter apt e",
                "first_name": "tom",
                "last_name": "marcy",
                "tel": "",
                "i_col": "businessleads",
                "i_db": "verifications-db",
                "db_type": "mongo",
                "name": "tom marcy"
            },
{
                "_id": "5a8fdb712467a7bb10ff1881",
                "email": "tmarcy@yahoo.com",
                "company_name": "Ymca",
                "title": "Executive Director",
                "linkedin account": "tmarcy",
                "city": "kansas city",
                "state": "mo",
                "zip": 64154,
                "fax": 8168108899,
                "company_website": "chemungymca.org",
                "email_lower_sha256": "8cba87b3d76d1792a018f2a7898f26d5200c0dfe7e0ec939e6aa12e19b3752f0",
                "addr_01": "3933 nw 85th ter apt e",
                "first_name": "tom",
                "last_name": "marcy",
                "tel": "",
                "i_col": "businessleads",
                "i_db": "verifications-db",
                "db_type": "mongo",
                "name": "tom marcy"
            }
]
def clean_data( res):
   props = {
      "email": [],
      "tel": []
   }
   for index in range(len(res)):
      one = res[index]
      email = one.get("email")
      # 如果一条数据有email属性
      if email:
         flag = False
         for i in range(len(props["email"])):
            # 有就加入所在序号,没有重新添加
            if email == props["email"][i]["value"]:
               props["email"][i]["position"].append(index)
               flag =True
         if not flag:
            props["email"].append({"position": [index,], "value": email})
   print(props)
def merge_data(dict1,dict2):
   merge_one = {}
   for k1, v1 in dict1.items():
      for k2, v2 in dict2.items():
         if k1 == k2:
            if v1 == v2:
               merge_one[k1] = v1
            else:
               merge_one[k1] = [v1, v2]
      if k1 not in dict2:
         merge_one[k1] = v1
   for k2, v2 in dict2.items():
      if k2 not in dict1.keys():
         merge_one[k2] = v2
   print(merge_one)
   return merge_one
def merge_all(li,res):
   li = []



dic= [
   {"a":1,
    "b":2,
    "c":5
    },
   {"a": 1,
    "b": 3,
    "d":89
    }
]
merge_data(dic[0],dic[1])
clean_data(res)