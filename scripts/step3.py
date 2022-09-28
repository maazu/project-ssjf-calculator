import argparse
from decimal import Decimal, getcontext
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool

getcontext().prec = 10000
getcontext().Emax = 999999999999999999

CAL_OPERATION = 'step3'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def compute_squareroot_cap(testnumber):
    testnumber = Decimal(testnumber)
    result = testnumber + 1
    result = result / 2
    return result


def compute_bndc(testnumber):

    result = round(Decimal(testnumber).sqrt())
    return result


def compute_step_three(testnumber, save_file, display_output, path=DEFAULT_RESULT_SAVE_PATH):

    print('Running Step 3 Script')

    square_root_cap = compute_squareroot_cap(testnumber)
    bndc = compute_bndc(testnumber)
    if save_file:
        content = 'SquarRootCap === > ' + \
            str(square_root_cap) + '\nBNDC === > ' + str(bndc)

        save_data_file(data_content=content, path=path)

    if display_output:
        print("Squarerootcap =>", str(square_root_cap))
        print("BNDC => ", str(bndc))

    return square_root_cap, bndc


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Execute Step 3 of the program.')

    parser.add_argument('--testnumber', type=str,
                        help='Enter a testnumber')

    parser.add_argument("--savefile", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    parser.add_argument("--showoutput", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    args = parser.parse_args()

    testnumber = args.testnumber
    display_output = args.showoutput
    save_file = args.savefile

    if testnumber.endswith('.txt'):
        testnumber = read_file_content(testnumber)

    # compute
    compute_step_three(testnumber, save_file=save_file,
                       display_output=display_output)
