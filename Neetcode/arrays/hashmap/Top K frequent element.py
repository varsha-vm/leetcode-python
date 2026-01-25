#Time: O(N)
#Space : O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        counter = 0


        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1

        for num, count in hashmap.items():
            freq[count].append(num)

        for i in range(len(nums), -1, -1):
            if len(freq[i])!=0 and counter!=k:
                res.extend(freq[i])
                counter+=len(freq[i])
        
        return res