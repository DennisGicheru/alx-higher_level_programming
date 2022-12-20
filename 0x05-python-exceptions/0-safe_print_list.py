#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    n = 0
    if my_list is None:
        return None
    else:
        for i in range(0, x):
            try:
                print("{}".format(my_list[i]), end="")
                n += 1
                if n >= x:
                    break
            except:
                continue
        print("")
        return(n)
