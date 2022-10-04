
from step3 import compute_squareroot_cap
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
from decimal import Decimal, getcontext
import argparse
import sys
from decimal import *
import collections
sys.float_info.max
getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999


CAL_OPERATION = 'step4'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def find_mod_equal_value(dict, query_value):
    return [key for key, value in dict.items() if value == query_value]


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
    print(unique_mods)
    found_pair = []
    subtracted_mods = []
    for number in unique_mods:
        for same_number in unique_mods:

            subtracted_number = same_number - number
            if subtracted_number >= 0:
                print(same_number, '-', number, '=', subtracted_number)
                subtracted_mods.append(subtracted_number)

            if subtracted_number < 0:
                new_remoded_number = subtracted_number % mod_number
                print(same_number, '-', number, '=',
                      subtracted_number, 'Result is less than zero', '{} will be remoded again by {} ==>'.format(subtracted_number, mod_number), new_remoded_number)
                subtracted_mods.append(new_remoded_number)
                subtracted_number = new_remoded_number

            if subtracted_number == final_check_number:
                print("====> This pair should be selected", same_number, number)
                found_pair.append(same_number)
                found_pair.append(number)

    # print(modding_dict)

    final_found_pairs = {}

    for number in found_pair:
        s = find_mod_equal_value(modding_dict, number)
        final_found_pairs[number] = s

    print("Found pairs")
    final_found_pairs = collections.OrderedDict(
        sorted(final_found_pairs.items()))
    for i, k in final_found_pairs.items():
        print(i, "\t\t", k)


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
