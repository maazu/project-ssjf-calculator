from utils.read_file import read_file_content, save_data_file, current_timestamp
from decimal import *
getcontext().prec = 999999999999999999
getcontext().Emax = 999999999999999999

CAL_OPERATION = 'subtract'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'


def initialise_file_content(number):
    number = read_file_content(number)
    return number


def subtract(number_one_file, number_two_file, path=DEFAULT_RESULT_SAVE_PATH):
    number_one = read_file_content(number_one_file)
    number_two = read_file_content(number_two_file)
    result = Decimal(number_one) - Decimal(number_two)
    save_data_file(data_content=str(result), path=path)


if __name__ == "__main__":
    print('Running Add Script')

    # Test files
    pi = '../testCaseNumbers/bill/' + "bill-char.txt"
    pi_two = '../testCaseNumbers/bill/' + 'decimalp-bill-char.txt'

    # read_file(path)
    number_one_file = pi
    number_two_file = pi

    # compute
    subtract(number_one_file, number_two_file)
