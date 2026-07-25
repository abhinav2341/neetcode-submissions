class Solution:
    def maxArea(self, heights: List[int]) -> int:
        si=0
        ei=len(heights)-1
        res=0
        while si<=ei:
            minheight= min(heights[si],heights[ei])
            res=max(res,(minheight) * (ei-si))
            if minheight == heights[si]:
                si=si+1
            else:
                ei=ei-1
        return res