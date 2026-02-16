#Appraoch : Two pointer + Area of triangle
#Time: O(N)
#sPACE o(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max_area = 0

        while l<r:
            h = min(heights[l], heights[r])
            b = r - l
            area = h * b
            max_area = max(max_area, area)

            if heights[l] < heights [r]:
                l+=1
            else:
                r-=1

        return max_area
