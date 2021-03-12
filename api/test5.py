def array_dels(n_d_li,li):
    a_index = [i for i in range(len(li))]
    a_index = set(a_index)
    b_index = set(n_d_li)
    index = list(a_index - b_index)
    _res = [li[i] for i in index]
    return _res


print(array_dels([1, 3, 5], ["d", "f", "s", "fs", "Ff", "SFf", "Ss"]))