import os
import argparse
from datetime import datetime


def current_timestamp():
    TIMESTAMP = str(datetime.now().strftime("%Y-%m-%d-%I-%M-%S-%p"))
    return TIMESTAMP


def initialise_file_content(number):
    number = read_file_content(number)
    return number


def save_data_file(path, data_content):
    try:
        with open(path, 'w') as a:
            a.write(data_content)
        print('Result file has been written successfully')
    except Exception as e:
        print('Error', str(e))


def read_file_content(path):
    try:
        with open(path) as f:
            data = f.read()
            return data

    except Exception as e:
        print('File reading error occurred', str(e))
        return False


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == "__main__":
    print('File script')
    # Testing
    # path = '../../testNumbers/bill-char.txt'
    # read_file(path)
