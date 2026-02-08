class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        count = 0
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1

        for key, val in hashmap.items():
            freq[val].append(key)

        
        for i in range(len(nums),-1,-1):
            if freq[i]!=[] and count<k:
                res.extend(freq[i])
                count+=len(freq[i])

        return res