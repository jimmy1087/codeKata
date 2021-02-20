
'''
https://app.codesignal.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2

What is the total maximum value of the items you can take with you, 
assuming that your max weight capacity is maxW and you can't come back for the items later?
'''
def knapsackLight(v1, w1, v2, w2, W):
    return max( (w1<=W)*v1, (w2<=W)*v2, ((w1+w2)<=W)*(v1+v2) )

# w1<=W  if its True, True is equivalent to 1 so value can be multiply by * v1
# w1<=W  if False, False is equivalent to 0 so value will be Zero

print(knapsackLight(4,5, 3,4, 5)) #Max value to carry is 5, w1 has the biggest value... 4
print(knapsackLight(2,5, 3,4, 5)) #Max value you can get is by choosing v2 ... 3
print(knapsackLight(2,2, 3,3, 5)) #Max value is the sum since you can carry both
print(knapsackLight(2,6, 3,6, 5)) #Max value is zero
print(knapsackLight(20,5, 3,1, 5)) #Max value is 20