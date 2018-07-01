#!/usr/bin/python3

from yaml import load, dump


def traverse_compare_vals(val1, val2, parent):
    difs = []
    if type(val1) is dict:
        difs = traverse_compare_dicts(val1, val2, parent)
    elif type(val1) is list:
        difs = traverse_compare_lists(val1, val2, parent)
    else:
        if val1 != val2:
            difs.append(parent + "=" + str(val2))
    return difs


def traverse_compare_dicts(d1, d2, parent):
    difs = []
    for key, val in d1.items():
        if parent == "":
            p = key
        else:
            p = parent + '.' + key
        d = traverse_compare_vals(val, d2[key], p)
        if d:
            difs.extend(d)
    return difs


def traverse_compare_lists(l1, l2, parent):
    difs = []
    for i in l1:
        index = l1.index(i)
        p = parent + '[' + str(index) + '].'
        d = traverse_compare_vals(i, l1[l1.index(i)], p)
        if d:
            difs.extend(d)
    return difs


def compare_yamls(y1,y2):
    return traverse_compare_dicts(y1, y2, "")


if __name__ == '__main__':
    f1 = open('statefulset.yaml', 'r')
    f2 = open('statefulset2.yaml', 'r')
    data1 = load(f1)
    data2 = load(f2)
    differences = compare_yamls(data1, data2)
    print(differences)
