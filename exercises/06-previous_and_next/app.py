#Complete the function to return the previous and next number of a given numner.".
def previous_next(num):
    previous = num - 1
    next = num + 1
    return previous, next


#Invoke the function with any interger at its argument. 
print(previous_next(179))