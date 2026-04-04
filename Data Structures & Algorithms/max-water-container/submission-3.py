class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # brute force method

        best = 0

        for i in range(len(heights)):

            for j in range(len(heights)):

                if i != j:

                    w1, w2 = heights[i], heights[j]
                    water = min(w1, w2) * (j - i)

                    best = max(best, water)

        return best