class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        
        if k == len(cardPoints):
            return total
        
        n = len(cardPoints)
        
        res = float('-inf')
        
        m = n - k
        sum_nums = 0
        
        for i in range(m - 1):
            sum_nums += cardPoints[i]
            
        left = 0
        right = m - 1
        while right < n:
            sum_nums += cardPoints[right]
            
            res = max(res, total - sum_nums)
            
            sum_nums -= cardPoints[left]
            
            left += 1
            right += 1
            
        return res