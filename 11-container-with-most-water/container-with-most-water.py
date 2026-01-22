class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        max_area = 0
        while i < j:
            shortest_line_height = min(height[i], height[j])
            width = j-i
            area = width*shortest_line_height
            max_area = max(max_area, area)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_area
   