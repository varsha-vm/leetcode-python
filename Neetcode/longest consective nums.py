#Time: O(N)
#Space: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashset = set(nums)

        for num in hashset:
            prev = num - 1

            #beginning of timeline
            if prev not in hashset:
                cur_num = num
                cur_len = 0
                while cur_num in hashset:
                    cur_len += 1
                    cur_num = cur_num+1
                    

                longest = max(longest, cur_len)

        return longest