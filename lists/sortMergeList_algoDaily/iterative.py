'''
h1:  2 -> 6 -> 7 -> 8
h2:  1 -> 3 -> 4 -> 5 -> 9 -> 10
'''

def sortMergeLists(head1, head2):

    newNode = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.val < head2.val:
        newNode = head1  # Important to set a new Object to Head1
        newNode.next = sortMergeLists(head1.next, head2) # Next value will be returned from recursive call
    else:
        newNode = head2
        newNode.next = sortMergeLists(head1, head2.next)
    
    return newNode

'''
h1:  2 -> 6 -> 7 -> 8
h2:  1 -> 3 -> 4 -> 5 -> 9 -> 10

h1: 2 h2: 1 sort(2, 3) -> 1
h1: 2 h2: 3 sort(6, 3) -> 2
h1: 6 h2: 3 sort(6, 4) -> 3
h1: 6 h2: 4 sort(6, 5) -> 4
h1: 6 h2: 5 sort(6, 9) -> 5
h1: 6 h2: 9 sort(7, 9) -> 6         ... etc... upward
h1: 7 h2: 9 sort(8, 9) -> 7         ... 7 -> 8 -> 9 -> 10
h1: 8 h2: 9 sort(-, 9) -> 8         ... 8 -> 9 -> 10
h1: - h2: 9                         return 9 -> 10          

Down.......................         ... Up ..............
'''
class LinkedList:

    def __init__(self, val):
        self.val = val
        self.next = None

    def insert(self, val):
        current = self
        while current.next is not None:
            current = current.next
        current.next = LinkedList(val)

def printList(head):
    a = []
    curNode = head
    while curNode.next is not None:
        a.append(curNode.val)
        curNode = curNode.next
    a.append(curNode.val)
    print(' -> '.join(map(str,a)))

n2, n6, n7, n8 = 2, 6, 7, 8
head1 = LinkedList(n2)
head1.insert(n6)
head1.insert(n7)
head1.insert(n8)
printList(head1)

n1, n3, n4, n5, n9, n10 = 1, 3, 4, 5, 9, 10
head2 = LinkedList(n1)
head2.insert(n3)
head2.insert(n4)
head2.insert(n5)
head2.insert(n9)
head2.insert(n10)
printList(head2)

sl = sortMergeLists(head1, head2)
printList(sl)