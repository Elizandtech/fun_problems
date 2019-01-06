
from multiplication_table_as_module import positiveinteger

def fibonacci_sequence(N, X=None):  ## Two parameters we need to evaluate to True; N and X, which has 2 options: to use or not to use
    fibsequence = [0,1]             ## start a list with known values
   
    while len(fibsequence) < N and ((X != None and (fibsequence[-1]+fibsequence[-2])<X) or X==None):      
        fibsequence.append(fibsequence[-1]+fibsequence[-2])          ## adds the next element to the list
    return fibsequence

def extract_evenvalues_inlist(L):
    evenvalue = list()
    for value in L:
        if value % 2==0:            
            evenvalue.append(value)     ## Make a new list of values
    
    return evenvalue
    
## The main function should call the other functions to execute the program
## ** MAKE EACH FUNCTION AN INDIVIDUAL ENTITY: **
    ## ** I do not need to invoke function(s) within other functions (i.e. do not call fibonacci_sequence function within extract_evenvalues_inlist function)**

def main():
    target_list = positiveinteger(input("Enter the number of values you want in the list: "))
    optarg = input("Enter stop number. If none, press Enter: ")

    ## Code to account for an Enter press(no second argument) == ''
    if optarg != '':
        optarg = positiveinteger(optarg)
    else:
        optarg = None

    fib = fibonacci_sequence(target_list, optarg)
   
    #print(fib) ##--test--
    evens = extract_evenvalues_inlist(fib)
    print(sum(evens))


if __name__=="__main__":        ## Runs the whole program (main) when directly called - command line. Guards against running main program when import is used.
    main()
