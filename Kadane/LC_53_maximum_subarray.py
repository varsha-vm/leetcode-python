#Dynamic kadane => Better to continue with previous or start from new (Deciding to keep or drop)
#Time: O(N)
#Space: O(1)
class Solution(object):
    def maxSubArray(self, nums):
        cur_sum = nums[0]
        max_sum = nums[0]
        
        for r in range(1, len(nums)):
            cur_sum = max(nums[r], nums[r]+cur_sum)
            max_sum = max(max_sum,cur_sum)
            

        return max_sum