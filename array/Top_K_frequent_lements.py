#Time : O(N log N)
#Space : O(N) => Usage of hashmap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num,0)+1

        sorted_data = sorted(hashmap.items(), key = lambda x: x[1], reverse = True)

        return [sorted_data[i][0] for i in range(k)]
