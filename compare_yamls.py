#!/usr/bin/python3

from yaml import load, dump


def traverse_compare_vals(val1, val2):
    difs = []
    if type(val1) is dict:
        difs = traverse_compare_dicts(val1, val2)
    elif type(val1) is list:
        difs = traverse_compare_lists(val1, val2)
    else:
        if val1 != val2:
            difs.append(val2)
    return difs


def traverse_compare_dicts(d1, d2):
    difs = []
    for key, val in d1.items():
        d = traverse_compare_vals(val, d2[key])
        if d:
            difs.extend(d)
    return difs


def traverse_compare_lists(l1, l2):
    difs = []
    for i in l1:
        d = traverse_compare_vals(i, l2[l1.index(i)])
        if d:
            difs.extend(d)
    return difs


def compare_yamls(y1,y2):
    return traverse_compare_dicts(y1, y2)


if __name__ == '__main__':
    f1 = open('statefulset.yaml', 'r')
    f2 = open('statefulset2.yaml', 'r')
    data1 = load(f1)
    data2 = load(f2)
    differences = compare_yamls(data1, data2)
    print(differences)

    if data2['metadata']['name'] in differences:
        print('Excellent!')
