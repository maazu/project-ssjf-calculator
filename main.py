
from decimal import *
from test import TESTNUMBER, MOD_LIMITS_LIST, MOD_NUMER
import sys
sys.float_info.max

testnumber = TESTNUMBER
mod_number = MOD_NUMER
given_mod_limits = MOD_LIMITS_LIST
old_modnumber = -1
print('Testnumber ==>', testnumber)


square_root_cap = (testnumber + 1) // 2

unique_mods = [i*i % mod_number for i in range(1, mod_number)]
unique_mods = list(set(unique_mods))
testmod = testnumber % mod_number
bndc = round(Decimal(testnumber).sqrt())
smallest_mods = []

print('Unique mods ==>', unique_mods)
print('BNDC mods ==>', bndc)
print('Mod by Testnumber ==>', testmod)
print('Square root cap ==>', square_root_cap)


def subtraction_process(unique_mods):
    pairs = []
    for number_one in unique_mods:
        for number_two in unique_mods:
            result = (number_two - number_one) % mod_number
            if result == testmod:
                pairs.append({number_two, number_one})
    return pairs


def unique_mod_subtraction(chain_one, chain_two):
    pairs = []
    for number_one in chain_two:
        for number_two in chain_one:
            result = number_two - number_one
            if result > 1 and result not in pairs:
                pairs.append(result)
                if result not in smallest_mods:
                    smallest_mods.append(result)
    return pairs


def generate_chain(number):
    chain = [i for i in range(
        1, mod_number) if i*i % mod_number == number]
    return chain


chains_pairs = subtraction_process(unique_mods)
print("Chain pairs", chains_pairs)


for pair in chains_pairs:
    pair = list(pair)
    # Column Q,R
    chain_one = generate_chain(pair[0])
    chain_two = generate_chain(pair[1])
    print("Pair Chain", pair, "==>", chain_one, chain_two)

    # Y, Z
    unique_mod_subtraction(chain_one, chain_two)

# Unique Mods all all AJ
smallest_mods.sort()
print("Smallest Mods", smallest_mods)
old_modnumber = mod_number
mod_number = smallest_mods[0]


def generate_chain_old(number):
    chain = [i for i in range(
        1, old_modnumber) if i*i % old_modnumber == number]
    return chain


def find_mod_in_chain(chain):
    temp_list = []
    for number in chain:
        print('New number chain', number)
        while True:
            for i in range(0, mod_number):
                if i != 0:
                    number = number + old_modnumber
                square = number * number
                chain_index_mod = square % mod_number
                print(number, square, chain_index_mod, "\t",
                      square < square_root_cap, "\t", testnumber % mod_number)
                if square < square_root_cap:
                    temp_list.append(chain_index_mod)
                # if square < square_root_cap and chain_index_mod == testnumber % mod_number:
                #     # print(chain, number, square, chain_index_mod)
                #     print(number, square, chain_index_mod,
                #           square < square_root_cap, "********************************")
                #     temp_list.append(chain_index_mod)
            break
    return temp_list


def find_anouther_mod():
    pass


check_new_mod = False

print('----------------------------------------------------------------')
while len(smallest_mods) > 0:
    while True:
        mm = []
        for pair in chains_pairs:
            pair = list(pair)
            # Column Q,R
            chain_one = generate_chain_old(pair[0])
            chain_two = generate_chain_old(pair[1])
            print("Pair Chain", pair, "==>", chain_one, chain_two, mod_number)
            one = find_mod_in_chain(chain_one)
            two = find_mod_in_chain(chain_two)
            s = one+two
            for i in s:
                if s not in mm:
                    mm.append(s)
        sd = [element for element in mm[0] if element %
              mod_number == testnumber % mod_number]
        print(sd)
        if len(sd) == 0 and len(sd) == 0:
            print('Current mod could not produce any results', mod_number)
            smallest_mods.pop(0)
            mod_number = smallest_mods[0]
            print('================================')
        else:
            data = list(set(one+two))
            print('unique values', data)
            for value in data:
                for s in data:
                    re = s-value
                    print(s, value, re, re % mod_number)
            print('Modable value calculated', mod_number)
            break
    break
