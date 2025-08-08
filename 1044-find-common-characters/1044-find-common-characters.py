class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        count=Counter(words[0])
        for x in words:
            cur_cnt=Counter(x)
            for x in count:
                count[x]=min(cur_cnt[x],count[x])
        res=[]
        for x in count:
            for y in range(count[x]):
                res.append(x)
        return res











        # dict={}
        # for word in words:
        #     word=set(word)
        #     for x in word:
        #         if x in dict:
        #             dict[x]+=1
        #         else:
        #             dict[x]=1
        # return([x for x,y in dict.items() if y==len(words)])

        