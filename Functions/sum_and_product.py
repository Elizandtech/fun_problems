## Write a program that asks the user for a number n and gives them the option of computing the sum and computin the product of 1,...n. 

def sumsofanumber(N):
    try:
        number = int(N)
    except:
        raise ValueError("Invalid entry")
    if number <0:
        raise ValueError('Not a positive integer.')
    count =0
    for num in range(1, number+1):
        count = num + count
    return count

def productsofanumber(N):
    try:
        number = int(N)
    except:
        raise ValueError("Invalid entry")
    if number <0:
        raise ValueError('Not a positive integer.')
    product = 1
    for multiplier in range(1, number+1): 
        product = multiplier*product
    return product

try:
    integer = input("Enter a positive integer: ")
    choice = input("Do you want the sums or products (enter sum or product)?: ")
    if choice != 'sum' and choice !='product':
        quit()
except:
    print("Not valid.")
try:
    if choice =='sum':
        print("The sum of ",integer,"equals: ",sumsofanumber(integer))
    if choice=='product':
        print("The product of ",integer,"equals: ", productsofanumber(integer))
except Exception as e:
    print('Error:', str(e))


