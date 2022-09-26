from decimal import Decimal
from math import remainder
from .utils.file_upload import handle_fileupload, initialise_file_content


def unpack_payload(payload):
    number_one_path = handle_fileupload(payload, file_name='testNumberFile')
    number_two_path = handle_fileupload(payload, file_name='modlimits')
    number_one = initialise_file_content(number_one_path)
    number_two = initialise_file_content(number_two_path)
    return number_one, number_two


def compute_mod_limits(test_number, mod_limits_list):
    mod_found = False
    counter = 0
    mod_result = ''
    while not mod_found and counter < len(mod_limits_list):
        mod_by = Decimal(mod_limits_list[counter])

        mod = float(mod_by % test_number)
        mod_result = [number for number in mod_limits_list if Decimal(
            number.strip()) == mod]

        if len(mod_result) > 0:
            mod_found = True
            return mod_result[0]

        counter = counter + 1


def compute_step_two(request):
    '''
    Compute Mod limit 
    by checking if the limit 
    exist in the provided file
    '''
    number_one, number_two = unpack_payload(request)
    test_number = number_one
    mod_limits_list = number_two.split(',')
    test_number = Decimal(test_number)
    return compute_mod_limits(test_number, mod_limits_list)
