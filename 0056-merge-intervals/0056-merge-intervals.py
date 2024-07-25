class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        
        if n == 1:
            return intervals
        
        intervals.sort()
        
        ret = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > ret[-1][1]:
                ret.append(intervals[i])
                
            else:
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
                
        return ret
        