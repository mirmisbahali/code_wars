# My Solution
def digital_root(n):
    sum_of_digits = sum(int(number) for number in str(n))
    
    while (sum_of_digits > 9):
        sum_of_digits = sum(int(number) for number in str(sum_of_digits))
    
    return sum_of_digits


# Best Soluton
# def digital_root(n):
#     return n%9 or n and 9 


print(digital_root(16), 7)
print(digital_root(942), 6)
print(digital_root(132189), 6)
print(digital_root(493193), 2)
