'''
There is a numerical sequence known as “Triangular Numbers.” 
The pattern begins as 1, 3, 6, 10, 15, 21, and continues onward with the Nth number in the pattern, 
which is N plus the previous number. 
For example, the 7th number in the sequence is 28, since it’s 7 (which is N) 
plus 21 (the previous number in the sequence). 

Write a function that accepts a number for N and returns the correct number from the series. 
That is, if the function was passed the number 7, the function would return 28.
'''

def triangleNumbers(n):
    if n == 1:
        return 1
    return triangleNumbers(n-1) + n

print(triangleNumbers(7), 28)
print(triangleNumbers(8), 36)


'''
f(1) = 1
f(2) = f(1) + 2 = 3
f(3) = f(2) + 3 = 6
f(4) = f(3) + 4 = 10
f(5) = f(4) + 5 = 15
f(6) = f(5) + 6 = 21
f(7) = f(6) + 7 = 28 
f(8) = f(7) + 8 = 36
'''