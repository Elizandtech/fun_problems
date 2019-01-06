try:
    table=int(input("Enter table type (i.e. 12, 15,...up to 43): "))
    for i in range(0, table+1):
        print("%4d"%(i), end=" ")
    print('\n')
    for n in range(1, table+1):
        print("%4d"%(n), end=" ")
        for i in range(1, table+1):
            m=n*i
            print("%4d"%(m), end=" ")
        print('\n')
except:
    print("Didn't work")
