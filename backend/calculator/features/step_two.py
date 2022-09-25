from decimal import Decimal
from math import remainder
from .utils.file_upload import handle_fileupload


def compute_mod_limits(test_number, mod_limits_list):
    mod_found = False
    counter = 0
    mod_result = ''
    while not mod_found and counter < len(mod_limits_list):
        mod_by = Decimal(mod_limits_list[counter])
        print(test_number)
        mod = float(mod_by % test_number)
        mod_result = [number for number in mod_limits_list if Decimal(
            number.strip()) == mod]

        if len(mod_result) > 0:
            mod_found = True
            print("mode result", mod_result)
            print(mod_result)
            return mod_result[0]

        counter = counter + 1


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
    test_number = request.data['testNumber']
    test_number = Decimal(test_number)
    return compute_mod_limits(test_number, mod_limits_list)
