from django.views import View
from django.http import HttpResponse,JsonResponse
from .utils.sql import Database
from bson import ObjectId
import json

import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Searilizer():
    def __init__(self, rd):
        self.rd = rd

    def hander_rd(self):
        val = self.rd.get("val")
        type = self.rd.get("type")
        if not val or not  type:
            return None
        if type == 'name':
            first_n,mid_n,last_n = self.handle_name(val)
            if not mid_n and not last_n:
                con = {"f":{"first_name":first_n},
                       "m":{"middle_name":first_n},
                       "l": {"last_name":first_n},
                       "n":{"name":first_n}
                       }
                print("===>",con)
            else:
                _condi = {
                    "first_name":first_n,
                    "middle_name":mid_n,
                    "last_name":last_n,
                }
                con = {"spl_name":{},"all_name":{"name":val}}
                for key,val in _condi.items():
                    if val:
                        con["spl_name"][key] = val

            return con
        if type == 'tel':
            try:
                int_val = int(val)
            except Exception:
                int_val = None
            val = self.hander_tel_num(val)

            con = {
                "has_gang":{"tel":val},
                "no_gang":{"tel":int_val}
            }
            return con

        con = {
            type:val
        }
        return con
    def handle_name(self, name):
        r_list = name.split(' ')
        name_list = []
        for item in r_list:
            if item:
                name_list.append(item)
        if len(name_list) == 1:
            return (name_list[0], None, None)
        elif len(name_list) == 2:
            return (name_list[0], None, name_list[1])
        elif len(name_list) == 3:
            return (name_list[0], name_list[1], name_list[2])
    def hander_tel_num(self,num):
        n_li = list(num)
        if num[0] == '1':
            n_li.insert(1,'-')
            n_li.insert(5,'-')
            n_li.insert(9,'-')
        else:
            n_li.insert(3,'-')
            n_li.insert(7,'-')
        tel = "".join(n_li)
        return tel








class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        return json.JSONEncoder.default(self, o)


class InfoList(View):
    def get(self, request, version, *args, **kwargs):
        ser = Searilizer(request.GET)
        condition = ser.hander_rd()
        if not condition:
            res = {"errno":1,"msg":"未接收到有效数据"}
            return JsonResponse(res)
        db = Database()
        back_re = db.find(condition)
        if not back_re:
            res = {"errno":2,"msg":"没有查询到结果"}
            return JsonResponse(res)
        res = {
            "errno":0,
            "data":{
                "all_data":back_re,
                "count":len(back_re)
            }
        }
        json_res = json.dumps(res, cls=JSONEncoder)
        response = HttpResponse(json_res)
        response['content-type'] = 'application/json'
        return response
