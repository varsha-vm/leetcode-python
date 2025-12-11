#Approach : create one dict and iterate other over this
#Time: O(M+N)
#Space: 0(M)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        result = []

        for i in nums1:
            hashmap[i] = hashmap.get(i,0)+1   

        for i in nums2:
            if i in hashmap and hashmap[i]>0:
                hashmap[i]-=1
                result.append(i)
                
        return result