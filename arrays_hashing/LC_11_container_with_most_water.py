#Appraoch => Choose taller pole as width decreases.
#Time: O(N)
#Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0

        while l<r:
            h = min(height[l], height[r])
            w = r - l 
            area = h * w
            
            max_area = max(max_area, area)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1

        return max_area
