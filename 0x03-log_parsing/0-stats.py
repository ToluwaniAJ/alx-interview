#!/usr/bin/python3
"""Parsing log files with python"""

import re
import sys


def printf(codes, fsize):
    """Prints in the required format"""
    print("File size: {}".format(fsize))
    for k, v in sorted(codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


fsize = 0
codes = {'200': 0, '301': 0, '400': 0,
         '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
try:
    for i, line in enumerate(sys.stdin, 1):
        vals = line.split()
        if len(vals) > 3:
            code = vals[-2]
            if code in codes:
                codes[code] += 1
            fsize += int(vals[-1])
            if i % 10 == 0:
                printf(codes, fsize)
finally:
    printf(codes, fsize)