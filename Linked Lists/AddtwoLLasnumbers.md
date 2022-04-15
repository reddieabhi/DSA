## [Problem Link here](https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118786/offering/1381244)

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        
        self.data = data
        self.next = None

def addTwoLists(first, second):
	s1 = ''
	s2  = ''
	c1 = first
	c2 = second
	while c1 and c2:
		s1 += str(c1.data)
		c1 = c1.next
		s2 += str(c2.data)
		c2 = c2.next
	while c1:
		s1 += str(c1.data)
		c1 = c1.next
	while c2:
		s2 += str(c2.data)
		c2 = c2.next
	
	ans = 0
	ans = int(s1) + int(s2)
	ans = str(ans)
	res = None
	for i in range(len(ans)):
		if res is None:
			res = Node(int(ans[i]))
			res.next = None
			curr = res
		else:
			curr.next = Node(int(ans[i]))
			curr = curr.next
	return res
		
