def max_item(arr):
    res = float('-inf')
    
    for num in arr:
        res = max(res, num)
    return res

max_item([0, 1000, 100, 10, 10000])
