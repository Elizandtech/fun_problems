def summingmultiplesof3and5withinanumber(N):
    count =0
    try:
        num = int(N)
    except:
        raise ValueError('Not a valid integer')
    if num <0:
        raise ValueError('Not a positive integer.')
    while num >0:
        isdivisible = True
        num = num -1
        if num % 3!=0 and num % 5!=0:
            isdivisible = False
        elif num % 3==0 or num %5==0:
            count = num + count
    if isdivisible:
        return count

try:
    sumof = input('Enter a positive integer: ')
    print("The sum of the multiples of 3 and 5 within sumof is: ",summingmultiplesof3and5withinanumber(sumof))
except Exception as e:
    print("Error", str(e))
