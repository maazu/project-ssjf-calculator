
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
from decimal import Decimal, getcontext
import argparse
import sys
from decimal import *
import time
sys.float_info.max

getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999


CAL_OPERATION = 'generatenumber'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def generate_digits(number_type, pattern):
    join_str = ''
    if ',' in pattern:
        pattern = pattern.split(',')
        for index in range(len(pattern)-1):
            genernation_number = pattern[index]
            total_range = pattern[index+1]
            if index % 2 == 0:
                for iteration in range(0, int(total_range)):
                    join_str = str(join_str) + str(genernation_number)

        return join_str
    else:

        return str(pattern)


def generate_number(start_pattern, middle_pattern, ending_pattern, save_file, show_output, path=DEFAULT_RESULT_SAVE_PATH):
    start_time = time.time()
    start_pattern = generate_digits('start', start_pattern)
    middle_pattern = generate_digits('middle', middle_pattern)
    ending_pattern = generate_digits('ending', ending_pattern)
    result = start_pattern + middle_pattern + ending_pattern

    if save_file:
        save_data_file(data_content=str(result), path=path)

    if show_output:
        print(result)
    print(time.time() - start_time, "seconds took to complete the script")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate numbers ')

    parser.add_argument('--start', type=str,
                        help='Enter start number or start number file path')

    parser.add_argument('--middle', type=str,
                        help='Enter middle number or middle number file path')

    parser.add_argument('--ending', type=str,
                        help='Enter a ending number or ending number file path')

    parser.add_argument("--showoutput", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    parser.add_argument("--savefile", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    args = parser.parse_args()

    start_pattern = args.start or ''
    middle_pattern = args.middle
    ending_pattern = args.ending
    show_output = args.showoutput
    save_file = args.savefile

    if start_pattern.endswith('.txt'):
        start_pattern = read_file_content(start_pattern)

    if middle_pattern.endswith('.txt'):
        middle_pattern = read_file_content(middle_pattern)

    if ending_pattern.endswith('.txt'):
        ending_pattern = read_file_content(ending_pattern)

    # compute
    print('Running Generating numbers Script')
    generate_number(start_pattern, middle_pattern,
                    ending_pattern, save_file=save_file, show_output=show_output)
