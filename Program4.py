import math
numbers = input("D is : ")
numbers = numbers.split(',')
result = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result.append(Q)
print(result)
