import math
from decimal import Decimal
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
import argparse
import numba as nb
import sys
import sys
import numpy as np
max = sys.maxsize
sys.float_info.max
CAL_OPERATION = 'factorial'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


@nb.njit(fastmath=True, parallel=True)
def perform_operation(n):
    factorial = 1

    for i in nb.prange(1, int(n)+1):
        factorial = factorial * i
    return factorial


def compute_factorial(number_one, save_file, show_output, path=DEFAULT_RESULT_SAVE_PATH,):
    result = perform_operation(int(number_one))
    if save_file:
        save_data_file(data_content=str(result), path=path)

    if show_output:
        print(result)
    return result


if __name__ == "__main__":
    print('Running Factorial Script')

    parser = argparse.ArgumentParser(
        description='Execute Step 3 of the program.')

    parser.add_argument('--numberone', type=str,
                        help='Enter a number one')

    parser.add_argument("--savefile", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="save the result in file .")

    parser.add_argument("--showoutput", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    args = parser.parse_args()

    number_one = args.numberone
    save_file = args.savefile

    show_output = args.showoutput

    if number_one and number_one.endswith('.txt'):
        number_one = read_file_content(number_one)

    compute_factorial(number_one, save_file, show_output)
