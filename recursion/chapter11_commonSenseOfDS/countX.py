def countX(s):
    if len(s) == 0:
        return 0
    cnt = 0
    if s[0] == 'x':
        cnt += 1
    return cnt + countX(s[1:])

print('Count X in string, good way: ', countX('axxbxr'))



def countX(string, counter=0):
    if len(string) == 0:
        return 0
    if string[0] == 'x':
        counter += 1
    print(string, counter)
    return counter + countX(string[1:], counter)  # Passing the counter value as a parameter will bubble up and increment the counter


print('Count X in string incorrect way: ', countX('axxbxr',0))