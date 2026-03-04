class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = dict()
        

        for i in range(len(nums)):
            if nums[i] in hashset and abs(hashset[nums[i]]-i)<=k:
                return True

            hashset[nums[i]]=i

        return False

