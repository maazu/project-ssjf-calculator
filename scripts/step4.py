
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
from decimal import Decimal, getcontext
import argparse
import sys
from decimal import *
from numba import numba as nb
sys.float_info.max
getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999


CAL_OPERATION = 'step4'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def compute_step_four(testnumber, mod_number, save_file, display_output, path=DEFAULT_RESULT_SAVE_PATH):
    mod_results = []
    mod_number = int(mod_number)
    testnumber = Decimal(testnumber)
    for number in range(0, mod_number+1):
        mod = number % mod_number
        mod = mod * number
        if mod >= mod_number:
            mod_result = mod % mod_number
            mod_results.append(mod_result)
        else:
            mod_result = mod
            mod_results.append(mod_result)

    unique_mods = list(set(mod_results))

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

    print('Found Subtracted Mods \n', subtracted_mods)

    for number in range(0, mod_number+1):
        s = found_pair

    return found_pair


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
