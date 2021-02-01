def order_weight(strng):
    weights = strng.split(' ')

    def sumOfDigits(n):
        digits = list(map(int, n.strip()))
        return sum(digits)

    weights.sort(key=sumOfDigits)

    for i in range(len(weights)):
        if i < (len(weights)-1):
            if (sumOfDigits(weights[i]) == sumOfDigits(weights[i+1])):
                if (weights[i][0] > weights[i+1][0]):
                    print(weights[i], weights[i+1])
                    temp = weights[i]
                    weights[i] = weights[i+1]
                    weights[i+1] = temp
                    
    return ' '.join(weights)








print(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
# print(order_weight(""), "")