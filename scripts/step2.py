import argparse
from decimal import Decimal
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
import sys
from decimal import *
sys.float_info.max
getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999

CAL_OPERATION = 'step2'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def perform_operation(test_number, mod_limits_list):
    mod_found = False
    counter = 0
    mod_result = ''
    while not mod_found and counter < len(mod_limits_list):
        mod_by = Decimal(mod_limits_list[counter])

        mod = mod_by % test_number

        mod_result = [number for number in mod_limits_list if Decimal(
            number.strip()) == mod]

        if len(mod_result) > 0:
            mod_found = True
            return mod_result[0]

        counter = counter + 1


def compute_step_two(test_number, modlimit, save_file, display_output, path=DEFAULT_RESULT_SAVE_PATH):

    mod_limits_list = modlimit.split(',')
    test_number = Decimal(test_number)
    result = perform_operation(test_number, mod_limits_list)

    if save_file:
        save_data_file(data_content=str(result), path=path)

    if display_output:
        print("Modlimit Fount =>", str(result))

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Execute Step 3 of the program.')

    parser.add_argument('--testnumber', type=str,
                        help='Enter a testnumber')

    parser.add_argument('--modlimit', type=str,
                        help='Enter a testnumber')

    parser.add_argument("--savefile", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    parser.add_argument("--displayoutput", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    args = parser.parse_args()

    testnumber = args.testnumber
    modlimit = args.modlimit
    display_output = args.displayoutput
    save_file = args.savefile

    if testnumber and testnumber.endswith('.txt'):
        testnumber = read_file_content(testnumber)

    # compute
    compute_step_two(testnumber, modlimit, save_file=save_file,
                     display_output=display_output)
