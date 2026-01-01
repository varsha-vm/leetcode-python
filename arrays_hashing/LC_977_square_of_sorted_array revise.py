class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        pos = len(nums)-1
        output = [0]*len(nums)

        while pos>=0:
            squared_l = nums[l]**2
            squared_r = nums[r]**2

            if squared_r>squared_l:
                output[pos] = squared_r
                r-=1
            else:
                output[pos] = squared_l
                l+=1

            pos-=1
            

        return output

