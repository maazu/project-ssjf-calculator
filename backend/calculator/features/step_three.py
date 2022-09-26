from decimal import Decimal
from .utils.file_upload import handle_fileupload
from .basic_functions import unpack_payload, compute_addition, compute_exponent, compute_mutliplication, compute_squareroot, compute_subtraction, compute_division, compute_factorial
from .utils.file_upload import handle_fileupload, initialise_file_content


def compute_step_three(request):
    '''
    Check Mod limit
    '''

    number_one = unpack_payload(request)
    number_two = unpack_payload(request)
    print(number_one, number_two)
    return ''
