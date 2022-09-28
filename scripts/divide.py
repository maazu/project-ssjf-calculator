import argparse
from .utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
import sys
from decimal import *
sys.float_info.max
getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999

CAL_OPERATION = 'divide'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def perform_operation(number_one, number_two):
    result = Decimal(number_one) // Decimal(number_two)
    return result


def divide(number_one, number_two, save_file, show_output, path=DEFAULT_RESULT_SAVE_PATH,):

    result = perform_operation(number_one, number_two)
    if save_file:
        save_data_file(data_content=str(result), path=path)

    if show_output:
        print(result)
    return result


if __name__ == "__main__":
    print('Running Divide Script')

    parser = argparse.ArgumentParser(
        description='Execute Step 3 of the program.')

    parser.add_argument('--numberone', type=str,
                        help='Enter a number one')

    parser.add_argument('--numbertwo', type=str,
                        help='Enter a number two')

    parser.add_argument("--savefile", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="save the result in file .")

    parser.add_argument("--displayoutput", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    args = parser.parse_args()

    number_one = args.numberone
    number_two = args.numbertwo
    save_file = args.savefile

    show_output = args.displayoutput

    if number_one.endswith('.txt'):
        number_one = read_file_content(number_one)

    if number_two.endswith('.txt'):
        number_two = read_file_content(number_two)

    divide(number_one, number_two, save_file, show_output)
