### [Problem Link](https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381872) 


def flipBits(arr, n):
    ones_count = 0
    curr = 0
    curr_max = 0
    for i in range(n):
        if arr[i] == 1:
            ones_count += 1
            arr[i] = -1
        if arr[i] == 0:
            arr[i] = 1
        else:
            arr[i] = -1
        curr += arr[i]
        curr_max = max(curr_max, curr)
        if curr < 0:
            curr = 0

    return ones_count + curr_max
