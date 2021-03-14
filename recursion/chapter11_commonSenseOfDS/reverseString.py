def reverse(s):
    if len(s) == 1:
        return s
    return reverse(s[1:]) + s[0]    #Asume that the function -1 element will already be solved.

print('Reverse: abcde -->', reverse('abcde'))
