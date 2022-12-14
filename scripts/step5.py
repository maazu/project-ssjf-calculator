
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
from decimal import Decimal, getcontext
import argparse
import sys
from decimal import *

sys.float_info.max
getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999


CAL_OPERATION = 'step5'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def compute_step_four(testnumber, save_file, display_output, path=DEFAULT_RESULT_SAVE_PATH):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Execute Step 3 of the program.')

    parser.add_argument('--testnumber', type=str,
                        help='Enter a testnumber')

    parser.add_argument("--modnumber", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    parser.add_argument("--showoutput", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    parser.add_argument("--savefile", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    args = parser.parse_args()

    testnumber = args.testnumber
    modnumber = args.modnumber
    display_output = args.showoutput
    save_file = args.savefile

    if testnumber.endswith('.txt'):
        testnumber = read_file_content(testnumber)

    # compute
    print('Running Step 5 Script')
    compute_step_four(testnumber, save_file=save_file,
                      display_output=display_output)
