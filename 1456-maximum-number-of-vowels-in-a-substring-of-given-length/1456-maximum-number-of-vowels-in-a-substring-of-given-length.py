class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        
        res = 0
        
        left = right = 0
        
        temp = 0
        
        while right < len(s):
            if s[right] in vowels:
                temp += 1
                
            if right - left + 1 == k:
                res = max(res, temp)
                if s[left] in vowels:
                    temp -= 1
                left += 1
                
                
            right += 1
            
            
        return res
                
        