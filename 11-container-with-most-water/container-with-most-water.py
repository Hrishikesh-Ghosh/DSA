class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area_ever = 0

        while left < right:
            width = right - left
            area_right_now = min(height[left], height[right])*width
            max_area_ever = max(max_area_ever, area_right_now)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return max_area_ever