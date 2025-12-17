#Time: O(N)
#Space: O(N)
class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        majority_elm = len(nums)//2
        
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1

            if hashmap[i] > majority_elm:
                return i
