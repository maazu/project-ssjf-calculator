import re
import sys
from decimal import Decimal
from decimal import getcontext
from .utils.file_upload import handle_fileupload
from .basic_functions import unpack_payload
from .utils.file_upload import handle_fileupload, initialise_file_content, qsort
from django.http import JsonResponse

sys.float_info.max
getcontext().prec = 100000
getcontext().Emax = 1000000000


def determine_distance_in_list(given_list):
    distance = []
    for i in range(len(given_list)-1):
        # print(given_list[i], given_list[i+1])
        d = abs(abs(given_list[i]) - abs(given_list[i+1]))
        distance.append(d)

    distance = sum(list(set(distance)))

    return distance


def compute_step_four_ints(number_one, mod_number):

    first_step = []
    first_mod_result = []
    for i in range(1, mod_number+1):
        first_mod = (i**2) % mod_number
        # first_mod = first_mod * i
        first_mod_result.append({i, first_mod})
        first_step.append(first_mod)

    # uniques values
    first_step = qsort(list(set(first_step)))

    pairs = []
    for number in first_step:
        for same_number in first_step:
            subtract_value = same_number - number
            if subtract_value == int(number_one) % mod_number:
                pairs.append(number)
                pairs.append(same_number)
                # {0: [i == first_mod == 0]}

    final_pairs = {key: [] for key in pairs}

    for i in range(1, mod_number+1):
        first_mod = (i**2) % mod_number
        if first_mod in final_pairs:
            final_pairs[first_mod].append(i)

    return final_pairs


def unpack_payload(payload):
    number_one_path = handle_fileupload(payload, file_name='testNumberFile')
    # number_two_path = handle_fileupload(payload, file_name='numberTwoFile')
    number_one = initialise_file_content(number_one_path)
    # number_two = initialise_file_content(number_two_path)
    return number_one


def compute_step_four(request):
    '''
    Check Mod limit
    '''

    number_one = unpack_payload(request)
    mod_number = 36
    result = compute_step_four_ints(number_one, mod_number)
    return JsonResponse(result)
