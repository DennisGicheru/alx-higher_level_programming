#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string is not None:
        roman_ints = [1, 5, 10, 50, 100, 500, 1000]
        roman_nums = ["I", "V", "X", "L", "C", "D", "M"]
        total = 0
        x = 0

        for i in roman_string:
            x += 1
            for j in range(0, len(roman_nums)):
                if i == roman_nums[j]:
                    total = total + roman_ints[j]
                
        return(total)
    else:
        return 0
