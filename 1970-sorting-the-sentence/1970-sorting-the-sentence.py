class Solution:
    def sortSentence(self, s: str) -> str:
        a=s.split()
        a=sorted(a,key=lambda x:x[-1])
        out=[]
        for x in a:
            out.append(x[:-1])
        out=" ".join(out)
        return out    
















        # a=s.split()
        # b=''
        # c=[]
        # d=(sorted(a,key=lambda x:x[-1]))
        # print(d)
        # for x in d:
        #     c.append(x[:-1])
        # print(c)
        # b=' '.join(c)
        # print(b)
        # return b
        