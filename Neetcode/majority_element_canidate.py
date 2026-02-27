class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        cand_vote_count = 0


        for my_vote in nums:

            if cand_vote_count==0:
                candidate = my_vote
                cand_vote_count+=1

            elif my_vote == candidate:
                cand_vote_count+=1

            else:
                cand_vote_count-=1

        return candidate
