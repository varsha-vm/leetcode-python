def swap_items(mylist, idx1, idx2):
    temp = mylist[idx1]
    mylist[idx1] = mylist[idx2]
    mylist[idx2] = temp
    return mylist

def pivot(mylist, pivot_idx, end_idx):
    swap_idx = pivot_idx
    pivot_value = mylist[pivot_idx]

    for i in range(pivot_idx+1, end_idx+1):
        if mylist[i] < pivot_value:
            swap_idx+=1
            swap_items(mylist, swap_idx, i)

    swap_items(mylist, pivot_idx, swap_idx)
    return swap_idx

def quick_sort(mylist, left, right):
    if left < right:
        pivot_index = pivot(mylist, left, right)
        quick_sort(mylist, left, pivot_index-1)
        quick_sort(mylist, pivot_index+1, right)

    return mylist

quick_sort([4, 100, 3, 1, 10, 2], 0, 5)

