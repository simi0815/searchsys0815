def concat(a,b):
    _res = []
    if isinstance(a,list):
        _res.extend(a)
    else:
        _res.append(a)
    if isinstance(b, list):
        _res.extend(b)
    else:
        _res.append(b)
    b = set(_res)
    b = list(b)
    return b

print(concat(1, [1,3,4]))




a=[0,1,2,3,4,"ds",6,7,8,9,11]

b = [5,6,4]

a_index = [i for i in range(len(a))]
a_index = set(a_index)
b_index = set(b)
index = list(a_index-b_index)
a = [a[i] for i in index]

print(a)
