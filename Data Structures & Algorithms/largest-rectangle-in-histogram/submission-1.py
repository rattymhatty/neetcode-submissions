class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, v in enumerate(heights):
            while stack and v < heights[stack[-1]]:
                j = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, width*heights[j])
            stack.append(i)
        while stack:
            j = stack.pop()
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, width*heights[j])
        return max_area