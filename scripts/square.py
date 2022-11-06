import argparse
from decimal import *
from utils.read_file import read_file_content, save_data_file, current_timestamp, str2bool
import sys
from decimal import *
sys.float_info.max
getcontext().prec = 1000
getcontext().Emax = 999999999999999999

from bisect import bisect_left

def take_closest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    return before, after



CAL_OPERATION = 'squareroot'
DEFAULT_RESULT_SAVE_PATH = '../results/' + CAL_OPERATION + \
    '/' + current_timestamp() + '-' + CAL_OPERATION + '.txt'



    # first_list = []
    # start = 20
    # for i in range(100):
    #     s = start + 8
    #     first_list.append(start)
    #     start = s
    # first_list = [12] + first_list
    # print(first_list)

    # sec_list = []
    # start = 4
    # for i in first_list:
    #     s = start + i
    #     sec_list.append(start)
    #     start = s
    # # sec_list = [4] + sec_list

    # print(sec_list)

def find_index(column_p,number):
    for item in range(0,len(column_p)):
        if column_p[item] == number:
            return item

# odd number leng 3
# number length is 4

# def perform_operation(number_one):
#     length = len(number_one)
#     first_few = number_one[:3]
#     first_few = Decimal(first_few)
#     column_p = [ ((number * 2) * number ) * 2 for number in range(0,100)]
#     before,after = take_closest(column_p,first_few)
#     d = find_index(column_p,before)
#     j = d+1
#     print(before,after,first_few)
         
#     sub_one = first_few - before
#     sub_two = after - first_few
#     print(sub_one,sub_two)
#     differnce = sub_two
#     if sub_one > sub_two:
#         differnce = sub_two
#         closest = after
#     else:
#         differnce =  sub_one
#         closest = before
#     print(differnce, closest)

#     before_d = before / 2
#     after_d = after / 2
#     print(before_d, after_d)

#     first_square_on = d
#     first_square_on = j
#     print(d*2,j*2)
#     print((d*2+j*2)/2)
#     print((d+j)/2)
#     print(d,j)
    
#     # closest = sub_one
#     # if sub_two > sub_one :
#     #     closest = sub_one
#     # print(closest)
#     return 0

def perform_operation(number_one):
    length = len(number_one)
    print(length)

    if length % 2 == 0:
        first_few_digits = 4
    else:
        first_few_digits = 3

    first_few = number_one[:first_few_digits]
    print(first_few)
    test_number = Decimal(first_few)
    first_few = Decimal(first_few)
    column_p = [ ((number * 2) * number ) * 2 for number in range(0,100)]
    before, after = take_closest(column_p,first_few)
    print(before,after)
    before_half = before / 2
    after_half = after / 2
    d = find_index(column_p,before)
    j = d+1

    l = (d*2+j*2) / 2 
    k = (d+j) / 2
    combined = (l*k)*2
    pairs = [[before, before_half,d*2,d],[combined,l*k,l,k], [after,after_half,j*2,j]]
    print(pairs)
    count = 0
    while True:
        print('----------------------------------------------------------------------')
        print("This is combined now ",combined)
        if combined < test_number:   
            combined = combined * 100
            combined_half = combined / 2
            i = l * 10
            j = k * 10
            
            combined = str(combined)
            combined = combined.split('.')
            combined_length = len(combined[0])
            combined = Decimal(combined[0])
            new_test_num = Decimal(number_one[:combined_length])
            after =  after * 100

            num1 = after - new_test_num
            num2 = new_test_num - combined
            print("Subtract one",after,new_test_num,num1)
            print("Subtract two",new_test_num,combined,num2)

            print('-----------New Range----------------')
            print(after,after/2,)
            print(combined,combined/2,i,j)
            #print(combined, combined_half,i,j) 
            test_number = new_test_num

            
            count = count + 1
            if count == 2:
                break
            
        else:
            print('Combined limit exceeded',combined, test_number)
            break

def squareroot(number_one, save_file, show_output, path=DEFAULT_RESULT_SAVE_PATH,):
    result = perform_operation(number_one)
    if save_file:
        save_data_file(data_content=str(result), path=path)

    if show_output:
        print(result)
    return result


if __name__ == "__main__":
    print('Running SquareRoot Script')

    parser = argparse.ArgumentParser(
        description='Execute Step 3 of the program.')

    parser.add_argument('--numberone', type=str,
                        help='Enter a number one')

    parser.add_argument('--numbertwo', type=str,
                        help='Enter a number two')

    parser.add_argument("--savefile", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="save the result in file .")

    parser.add_argument("--showoutput", type=str2bool, nargs='?',
                        const=True, default=False,
                        help="print the result.")

    args = parser.parse_args()

    number_one = args.numberone
    number_two = args.numbertwo
    save_file = args.savefile

    show_output = args.showoutput

    if number_one and number_one.endswith('.txt'):
        number_one = read_file_content(number_one)

    if number_two and number_two.endswith('.txt'):
        number_two = read_file_content(number_two)

   
    squareroot(number_one, save_file, show_output)



#  Squareroot the number ->  multiply the result by iteslf -> if result is greater then test number --> OK -> else --> increase the size of the testnumber by 1

#11728389174931700 / 800000000000000