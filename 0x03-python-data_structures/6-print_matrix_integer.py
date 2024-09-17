#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        for x in i:
            print ("{:d}".format(x), end=" " if x < len(i-1) else end = "\n")
