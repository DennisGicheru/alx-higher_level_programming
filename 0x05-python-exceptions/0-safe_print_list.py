#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    n = 0
    for i in my_list:
        try:
            print("{}".format(my_list[i-1]), end="")
            n += 1
            if n >= x:
                break
            else:
                continue
        except IndexError:
            print("error,index out of range")
        except TypeError:
            print("type error detected")
    print("")
    return(x)
