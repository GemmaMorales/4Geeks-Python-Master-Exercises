#Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
    a = num // 10
    b = num % 10
    return str(b) + str(a)
   
   
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(82))

