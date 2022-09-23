from decimal import Decimal
from decimal import getcontext
import numpy as np
import sys
sys.float_info.max


def unpack_payload(payload):
    number_one = payload['testNumber']
    number_two = payload['numberTwo']
    return number_one, number_two


def compute_addition(payload):
    number_one, number_two = unpack_payload(payload)

    result = number_one + number_two
    return result


def compute_subtraction(payload):
    number_one, number_two = unpack_payload(payload)
    result = number_one - number_two
    return result


def compute_mutliplication(payload):
    number_one, number_two = unpack_payload(payload)
    result = number_one * number_two
    return result


def compute_division(payload):
    number_one, number_two = unpack_payload(payload)
    result = number_one // number_two
    return result


def compute_squareroot(payload):
    number_one, number_two = unpack_payload(payload)
    number = Decimal(number_two)
    getcontext().prec = 10000
    result = number.sqrt()
    return result


def compute_squareroot_cap(payload):
    number_one, number_two = unpack_payload(payload)
    result = (number_one + 1) // 2
    return result


def compute_exponent(payload):
    number_one, number_two = unpack_payload(payload)
    return 'still in progress'


def compute_factorial(payload):
    number_one, number_two = unpack_payload(payload)
    return 'still in progress'
