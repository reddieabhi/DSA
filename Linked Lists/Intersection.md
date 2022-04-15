### [Problem Link](https://www.codingninjas.com/codestudio/problems/630457?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website)


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
 

def findIntersection(firstHead, secondHead) :
	if firstHead is None or secondHead is None:
		return -1
	l1  = 0
	l2 = 0
	curr1 = firstHead
	curr2 = secondHead
	while curr1 and curr2:
		l1 += 1
		l2 += 1
		curr1 = curr1.next
		curr2 = curr2.next
	while curr1:
		l1 += 1
		curr1 = curr1.next
	while curr2:
		l2 += 1
		curr2 = curr2.next
	h1 = firstHead
	h2 = secondHead
	if l1 < l2 :
		h1,h2 = h2,h1
	for i in range(abs(l2-l1)):
		h1 = h1.next
	
	while h1 and h2:
		if h1 == h2:
			return h1.data
		h1 = h1.next
		h2 = h2.next
		
	return -1
