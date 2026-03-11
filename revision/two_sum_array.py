#Time:O(N)
#Space:O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bank = dict()

        for i, num in enumerate(nums):
            remaining_to_pay = target-num
            if remaining_to_pay in bank:
                return [bank[remaining_to_pay], i]

            bank[num] = i