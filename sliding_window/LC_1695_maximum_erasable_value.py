#Appraoch: Sliding Window for max subarray (Set + Shink and remove from left)
#Time: O(N)
#space: O(N) => Set
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        l=0
        visited = set()
        max_sum = 0
        cur_sum = 0
        for r in range(len(nums)):
            while nums[r] in visited:
                visited.remove(nums[l])
                cur_sum-=nums[l]
                l+=1
                
            visited.add(nums[r])
            cur_sum+=nums[r]
            max_sum = max(max_sum, cur_sum)

        return max_sum
            
            

    


                

            

        