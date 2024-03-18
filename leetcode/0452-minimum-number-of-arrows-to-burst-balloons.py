class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        pts = sorted(points)
        cnt = 1
        i = 0
        start = pts[i][0]
        end = pts[i][1]
        i += 1
        while i < len(pts):
            if pts[i][0] >= start and pts[i][0] <= end:
                start = pts[i][0]
                end = min(pts[i][1], end)
            else:
                cnt += 1
                start = pts[i][0]
                end = pts[i][1]
            i+=1
        
        return cnt