def sumofanumber(N):
    count = 0
    try:
        num = int(N)   
        if num < 0:
            return ValueError("Not a positive number")
        while num >0:
            count = num + count
            num = num -1
        return count
    except:
        return ValueError("Didn't work.")

try:
    somenum = input("Enter a positive integer: ")
    print("The total sum of numbers up to number " + somenum + " is: ", sumofanumber(somenum))
except Exception as e:
    print("Error", e)

