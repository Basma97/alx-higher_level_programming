#!/usr/bin/python3
import lists.h
def print_list_integer(my_list=[]):
    length = len(my_list)

    for i in range (length):
        print("{:d}".format(my_list[i]))
