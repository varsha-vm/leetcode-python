#Time: O(N)
#Space: O(1)
class Solution:
    def swap(self, mylist, left, right):
        mylist[left], mylist[right] = mylist[right], mylist[left]
        return mylist


    def sortColors(self, nums: List[int]) -> None:
        l = 0
        r = len(nums)-1
        i = 0


        while i<=r:
            if nums[i]==0:
                self.swap(nums, i, l)
                l+=1

            elif nums[i]==2:
                self.swap(nums, r, i)
                r-=1
                i-=1

            i+=1
