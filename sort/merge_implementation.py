#Approach: Works on sorted two lists
#Time: O(N log N)
#Space: O(N)

def merge(list1, list2):
    l = 0
    r = 0
    res = []
    
    while l<len(list1) and r < len(list2):
        left_digit = list1[l]
        right_digit = list2[r]

        if right_digit < left_digit:
            res.append(right_digit)
            r+=1

        else:
            res.append(left_digit)
            l+=1

    while l<len(list1):
        res.append(list1[l])
        l+=1
        

    while r<len(list2):
        res.append(list2[r])
        r+=1


    return res


#To recursively split the list into two sorted list, which is futher fed into merge() to sort and merge.
def merge_sort(mylist):
    if len(mylist) == 1:
        return mylist 
        
    mid = len(mylist)//2
    left_elms = merge_sort(mylist[:mid])
    right_elms = merge_sort(mylist[mid:])

    return merge(left_elms, right_elms)


merge_sort([2,10,22,8,12,5,1,99,3])