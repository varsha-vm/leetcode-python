#Approach use hashmap to store all cumulative seen + initialize hashmap with 0:1
#Time:O(N)
#Space:O(N)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        cur_sum = 0

        for num in nums:
            cur_sum+=num

            if cur_sum - k in hashmap:
                count+=hashmap[cur_sum-k]

            hashmap[cur_sum] = hashmap.get(cur_sum, 0)+1

        return count
        