#Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(a):
    quotient = a // 10
    remainder = a % 10
    return quotient, remainder
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
