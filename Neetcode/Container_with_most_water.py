class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        max_area = 0

        while l<r:
            h = min(height[l], height[r]) 
            b = r - l 
            area = h*b
            max_area = max(max_area, area)

            #which pointer to move next?
            if height[r] > height[l]:
                l+=1

            else:
                r-=1


        return max_area