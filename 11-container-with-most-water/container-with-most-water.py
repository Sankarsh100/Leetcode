class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            # Height is limited by the shorter of the two lines
            h = min(height[l], height[r])
            # Width is the distance between pointers
            w = r - l
            # Update max area
            max_area = max(max_area, h * w)
            
            # Move the pointer at the shorter line inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
