class Solution:
    def isValid(self, s: str) -> bool:
        sta=[]
        mapping = {')': '(', '}': '{', ']': '['}
        for x in s:
            if x in mapping.values():
                sta.append(x)
            elif x in mapping.keys():
                if not sta or mapping[x]!=sta.pop():
                    return False
        return not sta
