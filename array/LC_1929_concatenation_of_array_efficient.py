#Time: O(N+N) => O(N)
#spaceL O(N)
class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for _ in range(2):
            for num in nums:
                ans.append(num)
        
        return ans


