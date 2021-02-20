'''
https://app.codesignal.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2

What is the total maximum value of the items you can take with you, 
assuming that your max weight capacity is maxW and you can't come back for the items later?
'''
def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if weight1 <= maxW:
        if value1 > value2:
            return value1
        elif weight2 <= maxW:
            return value2
        else:
            return value1
    if weight2 <= maxW:
        if value2 > value1:
            return value2
        elif weight1 <= maxW:
            return value1
        else:
            return value2
    return 0

print(knapsackLight(4,5, 3,4, 5)) #Max value to carry is 5, w1 has the biggest value... 4
print(knapsackLight(2,5, 3,4, 5)) #Max value you can get is by choosing v2 ... 3
print(knapsackLight(2,2, 3,3, 5)) #Max value is the sum since you can carry both
print(knapsackLight(2,6, 3,6, 5)) #Max value is zero
print(knapsackLight(20,5, 3,1, 5)) #Max value is 20