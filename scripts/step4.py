
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
from decimal import Decimal, getcontext
from decimal import *
import argparse
import numpy as np


CAL_OPERATION = 'step4'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def find_mod_equal_value(dict, query_value):
    return [key for key, value in dict.items() if value == query_value]


def compute_squareroot_cap(testnumber):
    testnumber = testnumber
    result = testnumber + 1
    result = result / 2
    return result


def compute_bndc(testnumber):
    s = np.sqrt([testnumber])
    result = round(s[0])

    return result


def find_sssssss(testnumber, found_pair, smallest_mod, modding_dict, mod_number):
    unique_mods = []
    for pair in found_pair:
        pair_split = pair.split('-')
        p1 = pair_split[0]
        p2 = pair_split[1]

        pair_val_1 = find_mod_equal_value(modding_dict, int(p1))
        pair_val_2 = find_mod_equal_value(modding_dict, int(p2))
        pair_val_1 = [number + mod_number for number in pair_val_1]
        pair_val_2 = [number + mod_number for number in pair_val_2]

        print(pair, pair_val_1, pair_val_2)

        for number_1, number_2 in zip(pair_val_1, pair_val_2):
            square_1 = number_1 * number_1
            resu1 = square_1 % smallest_mod
            square_2 = number_2 * number_2
            resu2 = square_2 % smallest_mod
            print(number_1, square_1, resu1, smallest_mod)
            print(number_2, square_2, resu2, smallest_mod)
            if resu1 >= 0:
                unique_mods.append(resu1)
            if resu2 >= 0:
                unique_mods.append(resu2)
    return list(set(unique_mods))


def subtraction_process(unique_mods, smallest_mod, testnumber):
    pairs = []
    for number_one in unique_mods:
        for number_two in unique_mods:
            result = number_two - number_one
            pair_mod = result % smallest_mod
            ch = int(testnumber % smallest_mod)
            if ch == pair_mod:
                print(number_two, '-', number_one, '\t',
                      result, '\t', ch)
                ss = str(number_two) + '-' + str(number_two)
                pairs.append(ss)


def compute_step_four(testnumber, mod_number, save_file, display_output, path=DEFAULT_RESULT_SAVE_PATH):
    mod_results = []
    mod_number = int(mod_number)

    testnumber = Decimal(testnumber)
    final_check_number = testnumber % mod_number
    modding_dict = {}
    src = compute_squareroot_cap(testnumber)
    bndc = compute_bndc(testnumber)
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

    all_smallest_mod_values = np.array([], dtype='int64')
    # Excel sheet process FINDING MODS AA
    bndc_limit_exceded = False
    for pair in found_pair:
        pair_split = pair.split('-')
        p1 = pair_split[0]
        p2 = pair_split[1]

        pair_val_1 = find_mod_equal_value(modding_dict, int(p1))
        pair_val_2 = find_mod_equal_value(modding_dict, int(p2))
        print(p2, pair_val_2, "--", p1, pair_val_1)
        all_results = np.array([], dtype='int64')
        for number_one in pair_val_1:
            for number_two in pair_val_2:
                subtract_out = number_two - number_one
                # print(number_two, number_one, subtract_out)
                if subtract_out > 1:
                    # print(number_two, number_one, subtract_out)
                    all_results = np.append(all_results, subtract_out)

            if len(all_results) > 0:
                found_smallest_mod = np.sort(all_results)
                smallest_value = found_smallest_mod[0]

                if smallest_value < bndc:
                    if smallest_value not in all_smallest_mod_values:
                        all_smallest_mod_values = np.append(
                            all_smallest_mod_values, smallest_value)

        print("Smallest Mod found in ", pair,
              smallest_value)
    smallest_mods_list = np.sort(all_smallest_mod_values)
    print('Smallest Mods Found ', smallest_mods_list)

    print("New chosen smallest Mod found", smallest_mods_list[0])

    another_unique_mods = {}

    for smallest_mod in smallest_mods_list:
        data = find_sssssss(testnumber, found_pair,
                            smallest_mod, modding_dict, mod_number)
        if (len(data) > 1):
            print(
                '\n====Performing subtraction using the unique values retrived with new mod ', smallest_mod, "======")
            print(data, "\n")
            s = subtraction_process(data, smallest_mod, testnumber)
            for pair in found_pair:
                pair_split = pair.split('-')
                p1 = pair_split[0]
                p2 = pair_split[1]
                pair_val_1 = find_mod_equal_value(modding_dict, int(p1))
                pair_val_2 = find_mod_equal_value(modding_dict, int(p2))
                pair_valone = [v+mod_number for v in pair_val_1]
                pair_valtwo = [v+mod_number for v in pair_val_2]

                print(pair_valtwo, pair_valone)
                for i1, i2 in zip(pair_valone, pair_valtwo):
                    print(i1, i2)
                break
        else:
            print(
                '\n\n ====Using the next smallest mode', smallest_mod, "====== \n\n")


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
