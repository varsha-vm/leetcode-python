#Using sliding window technique
#Time complexity : oO(N)
#Space complexity: O(K)

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        l = 0

        for r in range(len(nums)):
            dist = r-l
            if dist > k:
                visited.remove(nums[l])
                l+=1

            if nums[r] in visited:
                return True    

            visited.add(nums[r])

        return False