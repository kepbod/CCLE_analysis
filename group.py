#!/usr/bin/env python

import sys
from collections import defaultdict
import numpy


def main():
    check = sys.argv[1]
    gene = [x.rstrip() for x in open(sys.argv[2], 'r')]

    exp = defaultdict(dict)
    exp_list = defaultdict(list)

    with open(sys.argv[3], 'r') as f:
        for index, line in enumerate(f):
            if index <= 2:
                continue
            d, g = line.rstrip().split()[:2]
            e = line.rstrip().split()[2:]
            for n, i in enumerate(e):
                exp[g][n] = i
                exp_list[g].append(float(i))
    num = len(exp_list[check])
    order = numpy.argsort(exp_list[check])
    for n, o in enumerate(order):
        if n < round(num / 4):
            flag = '1'
        elif n >= round(num / 4 * 3):
            flag = '0'
        else:
            continue
        print('%s\t%s\t%s' % (check, flag, exp[check][o]))
        for og in gene:
            print('%s\t%s\t%s' % (og, flag, exp[og][o]))


if __name__ == '__main__':
    main()
