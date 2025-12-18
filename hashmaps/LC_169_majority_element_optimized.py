#Boyer–Moore Voting Algorithm
#Time: O(N)
#Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for i in nums:
            myvote=i
                
            if count==0:
                candidate=i
            if myvote==candidate:
                count+=1
            else:
                count-=1
    
        return candidate
