#!/usr/bin/python3
"""This file contains the python implementation of the
Pascal's Triangle"""


def pascal_triangle(n):
    """This function attempts to find the best way to calculate
    Pascal's triangle"""
    result = []
    if n <= 0:
        return []
    if n >= 1:
        result.append([1])
    if n >= 2:
        result.append([1, 1])
    if n > 2:
        for number in range(2, n):
            curr = result[-1]
            temp = [1]
            for num in range(1, number):
                value = curr[num - 1] + curr[num]
                temp.append(value)
            temp.append(1)
            result.append(temp)
    return result