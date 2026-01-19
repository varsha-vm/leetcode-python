#Approach: Works on sorted two lists
#Time: O(N log N)
#Space: O(N)

def merge_sort(list1, list2):
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

        
merge_sort([1,3,5,7,9],[0,2,4,6,8])