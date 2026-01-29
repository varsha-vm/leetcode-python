#Approach -> since alreayd sorted, two pointer is best. Further, LC need ans from index 1
#Time: O(N)
#Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            summation = numbers[l] + numbers[r]

            if summation == target:
                return [l+1,r+1]

            elif summation > target:
                r-=1
            else:
                l+=1

