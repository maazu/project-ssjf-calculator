import argparse
from decimal import Decimal
from genericpath import exists
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
import sys
from decimal import *
sys.float_info.max
getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999

CAL_OPERATION = 'step2'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def format_modlimt(numbers):
    if len(numbers) > 1:
        res = [int(number) for number in numbers.split(',')]
        return res
    else:
        return numbers


def check_availability_in_list(element, collection: iter):
    return element in collection


def perform_operation(test_number, mod_limits_list):
    mod_found = False
    number = 1
    while not mod_found:
        mod = Decimal(test_number) % number
        if check_availability_in_list(mod, mod_limits_list):
            return number
        number = number + 1


def compute_step_two(test_number, modlimit, save_file, display_output, path=DEFAULT_RESULT_SAVE_PATH):

    mod_limits_list = format_modlimt(modlimit)
    test_number = Decimal(test_number)
    result = perform_operation(test_number, mod_limits_list)

    if save_file:
        save_data_file(data_content=str(result), path=path)

    if display_output:
        print("Modlimit Found =>", str(result))

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

    if testnumber.endswith('.txt'):
        testnumber = read_file_content(testnumber)

    if modlimit.endswith('.txt'):
        testnumber = read_file_content(testnumber)

    # compute
    compute_step_two(testnumber, modlimit, save_file=save_file,
                     display_output=display_output)
