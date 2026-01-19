#Time: O(N LOG N)
#Space: O(N)
class Solution:
    def merge(self, sorted_left, sorted_right):
        l=0
        r=0
        res = []

        while l<len(sorted_left) and r<len(sorted_right):
            left_elm = sorted_left[l]
            right_elm = sorted_right[r]

            if right_elm < left_elm:
                res.append(right_elm)
                r+=1

            else:
                res.append(left_elm)
                l+=1

        while l<len(sorted_left):
            res.append(sorted_left[l])
            l+=1

        while r<len(sorted_right):
            res.append(sorted_right[r])
            r+=1

        return res

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums

        mid = len(nums)//2
        left_unsorted_elems = self.sortArray(nums[:mid])
        right_unsorted_elems = self.sortArray(nums[mid:])

        return self.merge(left_unsorted_elems, right_unsorted_elems)



        