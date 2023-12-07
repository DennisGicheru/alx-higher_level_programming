#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string is not None:
        rom_vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        int_val = 0
        n = roman_string
        for k in range(len(n)):
            if k > 0 and rom_vals[n[k]] > rom_vals[n[k - 1]]:
                int_val += rom_vals[n[k]] - 2 * rom_vals[n[k - 1]]
            else:
                int_val += rom_vals[n[k]]
        return (int_val)
    else:
        return 0
