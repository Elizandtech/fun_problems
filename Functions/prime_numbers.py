def convert_to_integer(inp):
    try:
        return int(inp)
    except:
        raise ValueError('Not and integer.')

def __number_greater_than(inp, minvalue):
    if inp < minvalue:
        raise ValueError('Less than two')
    else:
        return inp

def check_integer_value(inp, minvalue):
    num = convert_to_integer(inp)
    minval = convert_to_integer(minvalue)
    return __number_greater_than(num, minval)


def is_prime(inp):
    isprime = True
    for div in range(2, int(math.sqrt(inp)+1)):
        if inp % div== 0:
            isprime=False
            break
    return isprime


def print_prime_numbers(inp):
    for testnumber in range(2, inp+1):
        if is_prime(testnumber):
            print(testnumber)

def main():
    try:
        number = check_integer_value(input('Enter a positive integer: '),2)
        print_prime_numbers(number)
    except Exception as e:
        print('Error: ',str(e))

import math
if __name__=="__main__":
    main()
