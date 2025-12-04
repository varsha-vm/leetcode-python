#Time: O(N)
#Space: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()

        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in visited:
                return [i, visited[remaining]]

            visited[num] = i
