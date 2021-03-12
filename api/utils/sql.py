from pymongo import MongoClient
from .db_config import REFLECT
from .cid_refliect import CID_REFLECT
MONGO_ADDRESS = '192.168.1.231'
MONGO_PORT = 27017


class Database(object):
    def __init__(self, address=MONGO_ADDRESS, port=MONGO_PORT):
        self.conn = MongoClient(host=address, port=port, serverSelectionTimeoutMS=3000000)

    def get_state(self):
        return self.conn is not None

    def find(self, condition):
        #查询condition情况

        if len(condition) >= 2:
            res = []
            for v in condition.values():
                print("将要查询:",v)
                _res = self._find_all(v)
                res = res + _res
        else:
            res = self._find_all(condition)
        return res

    def _find_all(self,condit):
        o_list = []
        #依次查询集合
        for db_col,info in REFLECT.items():
            db,col = db_col.split(".")
            # 参照映射表调整condition,使其查询时符合所在表的字段
            _con = condit.copy()
            for k,v in condit.items():
                if k in info.keys() :
                    if k != info[k]:
                        _con[info[k]] = _con[k]
                        _con.pop(k)
                else:
                    _con.pop(k)
            if not _con:
                continue
            #查询
            find_res = self._find(_con,db,col)
            #反映射操作，
            _res = []
            #按照映射关系循环
            for one_res in find_res:
                _one = one_res.copy()
                for k, v in info.items():

                    if k != v:
                        if k == "cid":
                            _one["ctype"] = CID_REFLECT.get(v)
                        _one[k] = one_res[v]
                        _one.pop(v)
                if "first_name" in _one.keys():

                    f_name = _one.get("first_name","")
                    f_name = str(f_name)
                    m_name = _one.get("middle_name","")
                    l_name = _one.get("last_name","")
                    name_list = [f_name,m_name,l_name]
                    try:
                        name_list.remove("")
                        name_list.remove("")
                        name_list.remove("")
                    except Exception:
                        pass
                    print(name_list)
                    t_name = " ".join(name_list)
                    _one["name"] = t_name
                _res.append(_one)
            #反映射结束
            #将每个表查询到的数据加到总结果中
            for i in _res:
                o_list.append(i)
        return o_list

    def _find(self,condition,db,col):
        res = self.conn[db][col].find(condition)
        #数据加工
        _res = []
        for one in res:
            one["i_col"] = col
            one["i_db"] = db
            one["db_type"] = "mongo"
            _res.append(one)
        return _res
    def clean_data(self,res):
        props = {
            "eamil":[{"position":[],"value":'xxx@.com'}],
            "tel":[{"position":[],"value":"xx@.com"}]
        }
        for index in range(len(res)):
            one = res[index]
            email = one.get("email")
            #如果一条数据有email属性
            if email:
                for item in props["email"]:
                    #有就加如所在序号
                    if email == item["value"]:
                        item

                props["email"].append({"postion":index,"value":email})







