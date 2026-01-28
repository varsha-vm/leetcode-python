#Time : O(N)
#Space : O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        count = 0
        idx_counter = [[] for i in range(len(nums)+1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1

        for key, val in hashmap.items():
            idx_counter[val].append(key)

        
        for i in range(len(nums),-1,-1):
            if idx_counter[i]!=[] and count<k:
                res.extend(idx_counter[i])
                count+=len(idx_counter[i])

        return res