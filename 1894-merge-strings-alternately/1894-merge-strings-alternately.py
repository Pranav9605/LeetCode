class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        for x in range(min(len(word1),len(word2))):
            result+=word1[x]+word2[x]
        return result + word1[x+1:]+word2[x+1:]  