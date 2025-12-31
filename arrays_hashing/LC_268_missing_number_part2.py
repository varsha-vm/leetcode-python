# Approach => LEN() + formula
# Time: O(N)
# Space: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n*(n+1)//2
        return total_sum - sum(nums)