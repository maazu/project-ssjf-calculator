from .utils.file_upload import handle_fileupload
from .basic_functions import compute_addition, compute_exponent, compute_mutliplication, compute_squareroot, compute_subtraction, compute_division, compute_factorial


def compute_mod_limits(mod_limits_list):
    return "Compute limits tomorrow"


def compute_step_two(request):
    '''
    Compute Mod limit 
    by checking if the limit 
    exist in the provided file
    '''
    file_path = handle_fileupload(request)
    file = open(file_path, "r")
    file = file.read()
    mod_limits_list = file.split(',')
    return compute_mod_limits(mod_limits_list)
