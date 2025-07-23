class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out=[]
        for indx,y in enumerate (words):
            if x in y:
                out.append(indx)
            print(indx,y)
        return out
        