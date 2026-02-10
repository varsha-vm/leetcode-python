#Approach : Use a hashset as dups does not matter and order does not matter.
#Time: O(N)
#Space : O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set =set(nums)
        longest = 0

        for num in nums_set:
            prev = num - 1

            #beginning of sequence
            if prev not in nums_set:
                cur_num = num
                cur_len = 1

                while cur_num + 1 in nums_set:
                    cur_num=(cur_num+1)
                    cur_len+=1


                longest = max(longest, cur_len)
 
        return longest

        