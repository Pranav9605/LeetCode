class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        # words=str(words)
        # a=words.split(separator)
        # return list(a)
        lst=[]
        for x in words:
            word=x.split(separator)
            for x in word:
                if (x!=""):
                    lst.append(x)
        return lst


        