#Approach -> Array + dict + prefixsum
#Time: O(N)
#Space: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        debt_recovery_book = {0:1}
        res = 0
        cur_gained = 0

        for money in nums:
            cur_gained+=money
            balance = cur_gained - k

            if balance in debt_recovery_book:
                res+=debt_recovery_book[balance]

            debt_recovery_book[cur_gained] = debt_recovery_book.get(cur_gained, 0)+1

        return res
            