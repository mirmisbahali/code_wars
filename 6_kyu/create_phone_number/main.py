# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    numStr = ''.join([str(el) for el in n])
    ph = '(' + numStr[:3] + ') ' + numStr[3:6] + '-' + numStr[6:]
    return (ph)


'''
This is clever'

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    
'''



print("Basic tests")
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
print(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
print(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")