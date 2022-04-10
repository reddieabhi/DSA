### [Sort 0 1 2](https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381875)

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr,n):
    l = 0
    m = 0
    h = n - 1
    while arr[h] == 2 and h >= 0:
        h = h -1
    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 1:
            m += 1
        elif arr[m] == 2:
            arr[h], arr[m] = arr[m], arr[h]
            while arr[h] == 2:
                h = h - 1
    return arr
            

#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
