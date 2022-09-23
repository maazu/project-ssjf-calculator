from .utils.file_upload import handle_fileupload
from .basic_functions import compute_addition, compute_exponent, compute_mutliplication, compute_squareroot, compute_subtraction, compute_division, compute_factorial


def compute_step_two(payload):
    '''
    Check Mod limit
    '''
    file = handle_fileupload(payload)
    print(file)
    return ''
    