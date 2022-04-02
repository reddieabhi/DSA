### [Problem link](https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381870)



```
def maxSubarraySum(arr, n):
    curr_sum = 0
    curr_max = 0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum >= curr_max:
            curr_max = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return curr_max
```
