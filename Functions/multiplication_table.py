# Write a program that prints a multiplication table.
# Functions are for single unit tasks. Make a function for the printheader and the sequence(innerds of the table).

def positiveinteger(N):
    try:
        posnum = int(N)
    except:
        raise ValueError('Not an integer.')
    if posnum <0:
        raise ValueError('Less than 0')
    else:
        return posnum

def printsequenceintable(N, I):
    maxnumber = positiveinteger(N)
    for column in range(1, maxnumber+1):
        product=I*column
        print("%4d"%(product), end=" ")

def printnewheader(N):
    print("%4s"%('x'), end=" ")
    printsequenceintable(N,1)

def printmultiplicationtable(N):
    maxnumber = positiveinteger(N)
    printnewheader(maxnumber)
    for rowid in range(1, maxnumber+1):
        print("\n")
        print("%4d"%(rowid), end=" ")
        printsequenceintable(maxnumber, rowid)

try:
    inp = input("Enter table type(i.e. 12, 15, etc.) up to 37: ")
    printmultiplicationtable(inp)
except Exception as e:
    print("Error:", str(e))
   
