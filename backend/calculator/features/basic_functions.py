from decimal import Decimal
from decimal import getcontext
import numpy as np
import sys
import mpmath as mpf
from .utils.file_upload import handle_fileupload, initialise_file_content
import numba as nb
sys.float_info.max

'''
Payload Doc

number_one : testNumber
number_two : numberTwo

'''


def unpack_payload(payload):
    number_one_path = handle_fileupload(payload, file_name='testNumberFile')
    number_two_path = handle_fileupload(payload, file_name='numberTwoFile')
    number_one = initialise_file_content(number_one_path)
    number_two = initialise_file_content(number_two_path)
    return number_one, number_two


def compute_addition(payload):
    number_one, number_two = unpack_payload(payload)
    number_one = number_one.replace('.', '')
    number_two = number_two.replace('.', '')
    getcontext().prec = 1000
    getcontext().Emax = 1000000000

    result = Decimal(number_one) + Decimal(number_two)

    return result


def compute_subtraction(payload):
    number_one, number_two = unpack_payload(payload)
    getcontext().prec = 10000
    getcontext().Emax = 1000000000
    result = Decimal(number_one) - Decimal(number_two)

    return result


def compute_mutliplication(payload):
    number_one, number_two = unpack_payload(payload)
    getcontext().prec = 10000
    getcontext().Emax = 1000000000
    result = Decimal(number_one) * Decimal(number_two)

    return result


def compute_division(payload):
    number_one, number_two = unpack_payload(payload)
    getcontext().prec = 1000
    getcontext().Emax = 1000000000
    result = Decimal(number_one) // Decimal(number_two)
    return result


def compute_squareroot(payload):
    number_one, number_two = unpack_payload(payload)
    getcontext().prec = 10000
    getcontext().Emax = 1000000000
    result = Decimal(number_one).sqrt()
    return result


def factorial(x):
    n = 1
    for i in range(2, x+1):
        n *= i
    return n


def compute_factorial(payload):
    number_one, number_two = unpack_payload(payload)

    number_one = int(number_one)
    result = factorial(number_one)

    return result


def compute_exponent(payload):
    number_one, number_two = unpack_payload(payload)
    return 'still in progress'
