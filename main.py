class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        final = True
        for i in list(ransomNote):
            if i in magazine:
                index = magazine.find(i)
                magazine = magazine[:index] + magazine[index+1:]
            else :
                final = False
                
        return final

solution = Solution()

ransomNote = "aa"
magazine = "aab"
result = solution.canConstruct(ransomNote, magazine)
print(result)
