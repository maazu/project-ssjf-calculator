
from step3 import compute_squareroot_cap
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
from decimal import Decimal, getcontext
import argparse
import sys
from decimal import *
import collections
import numpy as np
from numba import jit
import random
import timeit
import numpy as np
import pandas as pd
sys.float_info.max
getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999


CAL_OPERATION = 'step4'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def find_mod_equal_value(dict, query_value):
    return [key for key, value in dict.items() if value == query_value]


@jit
def merge(l1, l2):
    combined = []
    c1 = 0
    c2 = 0
    n1 = l1[c1]
    n2 = l2[c2]
    len1 = len(l1)
    len2 = len(l2)
    while (c1 < len1 and c2 < len2):
        if n1 < n2:
            combined.append(n1)
            c1 += 1
            if (c1 < len1):
                n1 = l1[c1]
        else:
            combined.append(n2)
            c2 += 1
            if (c2 < len2):
                n2 = l2[c2]
    combined.extend(l1[c1:])
    combined.extend(l2[c2:])
    return combined


@jit
def mergesort(a):
    n = len(a)
    if n == 0:
        return a
    if n == 1:
        return a
    if n > 1:
        return merge(mergesort(a[:int(n/2)]), mergesort(a[int(n/2):]))


def compute_step_four(testnumber, mod_number, save_file, display_output, path=DEFAULT_RESULT_SAVE_PATH):
    mod_results = []
    mod_number = int(mod_number)

    testnumber = Decimal(testnumber)
    final_check_number = testnumber % mod_number
    modding_dict = {}
    src = compute_squareroot_cap(testnumber)
    for number in range(0, mod_number+1):
        if number > src:
            break

        number_square = number * number
        mod = number_square % mod_number  # taking the mod

        if mod >= mod_number:
            mod_result = mod % mod_number
            mod_results.append(mod_result)
        else:
            mod_result = mod
            mod_results.append(mod_result)
        modding_dict[number] = mod_result

    unique_mods = list(set(mod_results))
    print("Unique Mods ", unique_mods)
    found_pair = []

    for number in unique_mods:
        for same_number in unique_mods:

            subtracted_number = same_number - number
            if subtracted_number >= 0:
                # print(same_number, '-', number, '=', subtracted_number)
                subtracted_number = subtracted_number

            if subtracted_number < 0:
                new_remoded_number = subtracted_number % mod_number
                # print(same_number, '-', number, '=',
                #       subtracted_number, 'Result is less than zero', '{} will be remoded again by {} ==>'.format(subtracted_number, mod_number), new_remoded_number)
                subtracted_number = new_remoded_number

            if subtracted_number == final_check_number:
                print("This pair should be selected",
                      same_number, number, final_check_number)

                found_pair.append(str(number) + "-" + str(same_number))

    print("Number where subtracted result found equal", found_pair)
    final_smallest_mod = 'not found'
    # Excel sheet process FINDING MODS AA
    for pair in found_pair:
        pair_split = pair.split('-')
        p1 = pair_split[0]
        p2 = pair_split[1]
        pair_val_1 = find_mod_equal_value(modding_dict, int(p1))
        pair_val_2 = find_mod_equal_value(modding_dict, int(p2))
        print(p1, pair_val_1, "--", p2, pair_val_2)

        for number_one in pair_val_1:
            all_results = np.array([], dtype='int64')
            for number_two in pair_val_2:
                subtract_out = number_two - number_one
                #print(number_two, number_one, subtract_out)
                if subtract_out > 1:
                    all_results = np.append(all_results, subtract_out)

            if len(all_results) > 0:
                found_smallest_mod = np.sort(all_results)
                smallest_value = found_smallest_mod[0]
                if final_smallest_mod == 'not found' and smallest_value > 0:
                    final_smallest_mod = smallest_value
                else:
                    if final_smallest_mod > smallest_value:
                        final_smallest_mod = smallest_value

            # print("Smallest Mod found in ", pair_val_2,
            #       found_smallest_mod[0])

    print("Final smallest Mod found", final_smallest_mod)

    print('Now we find the closest values in the gnerated pairs')


# 6 - 1 = 5
# 17 - 12 = 5


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Execute Step 3 of the program.')

    parser.add_argument('--testnumber', type=str,
                        help='Enter a testnumber')

    parser.add_argument("--modnumber",  type=str,
                        help='Enter a mod number')

    parser.add_argument("--showoutput", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    parser.add_argument("--savefile", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    args = parser.parse_args()

    testnumber = args.testnumber or ''
    modnumber = args.modnumber
    display_output = args.showoutput
    save_file = args.savefile

    if testnumber.endswith('.txt'):
        testnumber = read_file_content(testnumber)

    # compute
    print('Running Step 4 Script')
    compute_step_four(testnumber, modnumber, save_file=save_file,
                      display_output=display_output)
