class Solution:

    # My Solution using CarryOn is a little bit more complicated than the Tutorial but is a little bit faster.
    def plusOne_Mine(self, digits: List[int]) -> List[int]:
        carryOn = False
        firstLoop = True
        for x in range(len(digits)-1,-1,-1):
            print(x)
            if carryOn or firstLoop:
                digits[x] = digits[x] + 1
            if digits[x] > 9:
                carryOn = True
                digits[x] = 0
            else:
                break
        if digits[0] == 0:
            digits.append(1)
            return digits[::-1]
        else:
            return digits

    # Better solution - Tutorial schoolbook
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # move along the input array starting from the end
        for i in range(n):
            
            idx = n - 1 - i
            print(idx)
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits
                
        # we're here because all the digits are nines
        return [1] + digits