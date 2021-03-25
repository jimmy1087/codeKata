#https://www.algoexpert.io/questions/Phone%20Number%20Mnemonics

m = {0:['0'], 1:['1'], 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 
	 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

def phoneNumberMnemonics(phoneNumber, idx = 0):
	subsets = phoneNumberHelper(phoneNumber)
	#print(subsets)
	return list(filter(lambda x:len(x) == len(phoneNumber), subsets))
	
def phoneNumberHelper(phoneNumber, idx = 0):
	if idx == len(phoneNumber):
		return ['']
	subsets = phoneNumberHelper(phoneNumber, idx + 1)
	key = int(phoneNumber[idx])
	#print(key, m[key])
	nodes = subsets[:]
	for subset in nodes:
		for keyValue in m[key]:
			new = keyValue + subset
			subsets.append(new)
	return subsets

phoneNumber = '1905'
print(phoneNumberMnemonics(phoneNumber))