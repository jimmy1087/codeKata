#https://www.algoexpert.io/questions/Phone%20Number%20Mnemonics

m = {0:['0'], 1:['1'], 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 
	 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

def phoneNumbers(phoneNumber):
    r = []
    phoneNumbersHelper(phoneNumber, 0, r, [])
    return r

def phoneNumbersHelper(phoneNumber, idx, r, perm):
    if len(perm) == len(phoneNumber):
        r.append(''.join(perm))
        return
    keys = m[int(phoneNumber[idx])]
    for key in keys:
        newPerm = perm[:]
        newPerm.append(key)
        phoneNumbersHelper(phoneNumber, idx+1, r, newPerm)
    
phoneNumber = '1905'
print(phoneNumbers(phoneNumber))
'''
phoneNumber = '1905'

idx = 0   r = []        perm = []        newPerm = []        keys = 1 = [1]
                                         newPerm = [1]
idx = 1   r = []        perm = [1]       newPerm = [1]       keys = 9 = [w,x,y,z]
                                         newPerm = [1,w]
idx = 2   r = []        perm = [1,w]     newPerm = [1,w]     keys = 0 = [0]
                                         newPerm = [1,w,0]
idx = 3   r = []        perm = [1,w,0]   newPerm = [1,w,0]   keys = 5 = [j,k,l]     <- Makes a copy
                                         newPerm = [1,w,0,j]                        <- Creates permutation
idx = 4   r = ['1w0j']  perm = [1,w,0,j]
idx = 3   r = ['1w0j']  perm = [1,w,0]   newPerm = [1,w,0]                          <- Makes a copy again
                                         newPerm = [1,w,0,k]                        <- New permutation
idx = 4   r = ['1w0j']  perm = [1,w,0,k]                                 
... etc

'''