class Solution:

    # My Solution using CarryOn is a little bit more complicated than the Tutorial but is a little bit faster.
    # Runtime: 32 ms
    # Memory Usage: 13.8 MB
    # Time complexity : O(N)
    # Space complexity : O(1)
    def plusOne_A(self, digits: List[int]) -> List[int]:
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

    # Clear solution - Tutorial schoolbook - Although a little bit slower than mine
    # Runtime: 36 ms
    # Memory Usage: 13.8 MB
    # Time complexity : O(N)
    # Space complexity : O(1)
    def plusOne_B(self, digits: List[int]) -> List[int]:
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

    # Using Linked List
    # Runtime: 36 ms
    # Memory Usage: 13.7 MB
    # Time complexity : O(N)
    # Space complexity : O(1)
    def plusOne_LinkedList(self, digits: List[int]) -> List[int]:
        head = self.getListNodeFromList(digits)
        # sentinel head
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel
        
        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next 
        
        # increase this rightmost not-nine digit by 1
        not_nine.val += 1
        not_nine = not_nine.next 
        
        # set all the following nines to zeros
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
        
        s = sentinel if sentinel.val else sentinel.next
        return self.getListFromNodeList(s)
        
    def getListNodeFromList(self, digits: List[int]) -> ListNode:
        head = ListNode(digits[0])
        tail = head
        e = 1
        while e < len(digits):
            tail.next = ListNode(digits[e])
            tail = tail.next
            e+=1
        return head
    
    def getListFromNodeList(self, head: ListNode) -> List:
        r = []
        while head:
            r.append(head.val)
            head = head.next
        return r