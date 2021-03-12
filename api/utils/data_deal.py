class MeageData(object):
    def __init__(self, data):
        self.data = data

    def _concat(self, a, b):
        _res = []
        if isinstance(a, list):
            _res.extend(a)
        else:
            _res.append(a)
        if isinstance(b, list):
            _res.extend(b)
        else:
            _res.append(b)
        _res = set(_res)
        _res = list(_res)
        return _res

    def _merge_data(self, dict1, dict2):
        merge_one = {}
        for k1, v1 in dict1.items():
            for k2, v2 in dict2.items():
                if k1 == k2:
                    merge_one[k1] = self._concat(v1, v2)
            if k1 not in dict2:
                merge_one[k1] = v1
        for k2, v2 in dict2.items():
            if k2 not in dict1.keys():
                merge_one[k2] = v2
        if not merge_one.get("merge"):
            merge_one["merge"] = True
        return merge_one

    def _merge_all(self, li, res):
        merge_dict = {}

        for i in li:
            merge_dict = self._merge_data(merge_dict, res[i])

        return merge_dict

    def _array_dels(self, n_d_li, li):
        a_index = [i for i in range(len(li))]
        a_index = set(a_index)
        b_index = set(n_d_li)
        index = list(a_index - b_index)
        _res = [li[i] for i in index]
        return _res

    def clean_data(self):
        self._clean_by_prop("email")
        self._clean_by_prop("tel")
        for i in range(len(self.data)):
            self.data[i]["index"] = i+1
        return self.data
    def _clean_by_prop(self, prop):
        res = self.data
        e_list = []
        # 通过相同prop合并
        for index in range(len(res)):
            one = res[index]
            p = one.get(prop)
            # 如果一条数据有这个属性
            if p:
                flag = False
                for i in range(len(e_list)):
                    # 有就加入所在序号,没有重新添加
                    if p == e_list[i]["value"]:
                        e_list[i]["position"].append(index)
                        flag = True
                if not flag:
                    e_list.append({"position": [index, ], "value": p})
        mer_list = []
        need_del = []
        for need_mer in e_list:
            if len(need_mer["position"]) <= 1:
                continue
            mer_dic = self._merge_all(need_mer["position"], res)
            mer_list.append(mer_dic)
            need_del.extend(need_mer["position"])

        res = self._array_dels(need_del, res)
        for im in mer_list:
            res.append(im)

        self.data = res
