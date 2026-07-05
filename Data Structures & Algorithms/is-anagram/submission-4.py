class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for char in set(s):
                if s.count(char) != t.count(char):
                    return False

            else :
                return True
        
        else :
            return False