
#Approach: sort + multiple edge cases handling with two pointer 
#time: O(NlogN) for sorting + O(N^2) for two pointer approach => O(N^2)
#space: O(N) for sorting + O(1) for two pointer approach => O(N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            #skip if same numbers are there
            if i>0 and nums[i]==nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l<r:
                total = nums[i] + nums[l] + nums[r]

                if total<0:
                    l+=1
                elif total>0:
                    r-=1

                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l]==nums[l-1]:
                        l+=1

                    while l<r and nums[r]==nums[r+1]:
                        r-=1

        return res
                    
