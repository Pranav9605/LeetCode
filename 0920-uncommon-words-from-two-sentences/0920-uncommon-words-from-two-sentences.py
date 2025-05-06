class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a=s1.split(" ")+ s2.split(" ")
        b=Counter(a)
        c=[]
        for x in b:
            if b[x]<2:
                c.append(x)
        return c
        print(a)

        