import sys
from decimal import Decimal
from decimal import getcontext
from .utils.file_upload import handle_fileupload
from .basic_functions import unpack_payload
from .utils.file_upload import handle_fileupload, initialise_file_content
from django.http import JsonResponse

sys.float_info.max
getcontext().prec = 100000
getcontext().Emax = 1000000000


def step_three_response():
    pass


def unpack_payload(payload):
    number_one_path = handle_fileupload(payload, file_name='testNumberFile')
    # number_two_path = handle_fileupload(payload, file_name='numberTwoFile')
    number_one = initialise_file_content(number_one_path)
    # number_two = initialise_file_content(number_two_path)
    return number_one


def compute_squareroot_cap(number_one):
    getcontext().prec = 10000
    getcontext().Emax = 1000000000
    number_one = (Decimal(number_one) + 1)

    result = number_one / 2
    return result


def compute_step_three(request):
    '''
    Check Mod limit
    '''

    number_one = unpack_payload(request)
    bndc = Decimal(number_one).sqrt()
    square_root_cap = compute_squareroot_cap(number_one)
    result = {"squareRootCap": square_root_cap, 'BNDC': round(bndc)}
    return JsonResponse({"squareRootCap": square_root_cap, 'BNDC': round(bndc)})
