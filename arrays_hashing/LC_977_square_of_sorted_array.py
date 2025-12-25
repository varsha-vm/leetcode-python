#Time: O(N LOG N)
#Space: O(N)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            squared = nums[i]*nums[i]
            nums[i]=squared

        return sorted(nums)