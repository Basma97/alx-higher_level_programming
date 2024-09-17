#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(i) == 0:
            print()
        for x in i:
            print ("{:d}".format(x), end=" ")
        print ()
