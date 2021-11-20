# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = dict()
        tCounter = dict()
        
        for char in s:
            sCounter[char] = sCounter.get(char, 0) + 1
                
        for char in t:
            tCounter[char] = tCounter.get(char, 0) + 1
                
        return sCounter == tCounter
        
# optional solution        
#         sCounter = collections.Counter(s)
#         tCounter = collections.Counter(t)
        
#         return sCounter == tCounter
