class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        q = deque()
        
        ans = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            
            while q and temp > temperatures[q[-1]]:
                idx = q.pop()
                ans[idx] = i - idx
            
            q.append(i)
            
        return ans
            
        