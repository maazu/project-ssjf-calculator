from decimal import Decimal
from .utils.file_upload import handle_fileupload
from .basic_functions import compute_addition, compute_exponent, compute_mutliplication, compute_squareroot, compute_subtraction, compute_division, compute_factorial


def compute_step_three(request):
    '''
    Check Mod limit
    '''
    file_path = handle_fileupload(request)
    file = open(file_path, "r")
    file = file.read()
    mod_limits_list = file.split(',')
    test_number = request.data['testNumber']
    test_number = Decimal(test_number)

    return ''
