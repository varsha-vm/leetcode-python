#Time: O(N^2)
#Space: O(N)
class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for x in range(len(nums)):
            if x > 0 and nums[x]==nums[x-1]:
                continue
            
            y = x+1
            z = len(nums)-1

            while y<z:
                three_sum = nums[x] + nums[y] + nums[z]

                if three_sum < 0:
                    y+=1

                elif three_sum > 0:
                    z-=1

                else:
                    res.append([nums[x], nums[y], nums[z]])

                    y+=1
                    z-=1

                    while y<z and nums[y] == nums[y-1]:
                        y+=1

                    while y<z and nums[z]==nums[z+1]:
                        z-=1
        return res