class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        
        left = right = 0
        
        s = str(num)
        
        while right < len(s):
            
            if right - left + 1 == k:
                
                if int(s[left : right + 1]) != 0 and num % int(s[left : right + 1]) == 0:
                    res += 1
                left += 1
            right += 1
            
        return res
        