### [Problem Link](https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381873)

def kadanes(arr):
    curr = 0
    curr_max  = -10**9
    for i in range(len(arr)):
        curr += arr[i]
        if curr> curr_max:
            curr_max = curr
        if curr < 0:
            curr = 0
    return curr_max


def maxSubSumKConcat(arr, n, k):
    single_sum_max = kadanes(arr)
    brr = arr*2
    double_sum_max = kadanes(brr)
    for i in range(1,len(arr)):
        arr[i] = arr[i] + arr[i-1]
    arr_sum = arr[n-1]
    add_factor = max(arr)
    if k <2:
        ans = single_sum_max
    elif k >= 2:
        sm_ans = (arr_sum * (k-1)) + add_factor
        ans = max(single_sum_max,double_sum_max,sm_ans)
    return ans
