#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list2 = []
    for x in my_list:
        my_list2.append(True if x % 2 == 0 else False)
    return my_list2
