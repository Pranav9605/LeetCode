class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length=[]
        for x in words:
            for y in x:
                if chars.count(y) < x.count(y):
                    break
            else:
                length.append(len(x))
        return sum(length)
        

        