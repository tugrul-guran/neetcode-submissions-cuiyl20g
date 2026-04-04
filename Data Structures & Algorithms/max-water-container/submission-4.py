class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        best_water_amount = 0

        while left < right:
            
            h_l, h_r = heights[left], heights[right]
            water_amount = min(h_l, h_r) * (right - left)

            best_water_amount = max(best_water_amount, water_amount)

            if h_l < h_r:
                left += 1
            else:
                right -= 1

        return best_water_amount