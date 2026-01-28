#Approach acquired and in ledger problem (Hashmap + iter already gained money)
#Time: O(N)
#Space: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            balance_in_account = target - num

            if balance_in_account in hashmap:
                return [hashmap[balance_in_account], i]


            hashmap[num] = i