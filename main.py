
from decimal import *
import sys
sys.float_info.max

testnumber = 12345
mod_number = 36
square_root_cap = (testnumber + 1) // 2
given_mod_limits = []
unique_mods = [i*i % mod_number for i in range(1, mod_number)]
unique_mods = list(set(unique_mods))
testmod = testnumber % mod_number
print('Unique mods', unique_mods)
bndc = round(testnumber)
smallest_mods = []


def subtraction_process(unique_mods):
    pairs = []
    for number_one in unique_mods:
        for number_two in unique_mods:
            result = (number_two - number_one) % mod_number
            if result == testmod:
                pairs.append({number_two, number_one})
    return pairs


def chain_subtraction(chain_one, chain_two):
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


def check_mod_chain(chain):
    chain = [i for i in range(
        1, square_root_cap) if i*i > square_root_cap]
    return chain


chains_pairs = subtraction_process(unique_mods)


for pair in chains_pairs:
    pair = list(pair)
    chain_one = generate_chain(pair[0])
    chain_two = generate_chain(pair[1])
    pairs = chain_subtraction(chain_one, chain_two)

smallest_mods.sort()
print(smallest_mods)


def find_mod_in_chain(chain):
    temp_list = []
    temp_mod_number = smallest_mods[0]
    for number in chain:
        while True:
            square = number * number
            if square < square_root_cap:
                number = number + mod_number
                chain_index_mod = square % temp_mod_number
                if chain_index_mod == testnumber % temp_mod_number:
                    temp_list.append(chain_index_mod)
            elif square > square_root_cap:
                break
    return temp_list


def smallest_mod_find():
    chains = []
    for pair in chains_pairs:
        pairing = list(pair)
        chain_one = generate_chain(pairing[0])
        chain_two = generate_chain(pairing[1])
        chain_one = find_mod_in_chain(chain_one)
        chain_two = find_mod_in_chain(chain_two)

        if len(chain_one) > 0 and len(chain_two) > 0:
            print(chain_one, chain_two)
            chains.append(chain_one)
            chains.append(chain_two)

            print("smallest_mods", smallest_mods[0])
            return True

    if len(chains) == 0:
        smallest_mods.pop(0)
        return False


print('================================')

while True:
    found = smallest_mod_find()
    if found:
        break
