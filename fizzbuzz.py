## create program that counts to 50. If a number is divisible by 3 print fizz. If divisible by 5 print buzz. If divisible by both print fizzbuzz.

for num in range(1,51):
    if num % 3==0:
        print('Fizz')
    elif num % 5==0:
        print('Buzz')
    elif num % 3==0 and num % 5==0:
        print('FizzBuzz')
    else: 
        print(num)
