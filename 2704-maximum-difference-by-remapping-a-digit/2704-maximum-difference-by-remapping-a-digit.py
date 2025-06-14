class Solution:
    def minMaxDifference(self, num: int) -> int:
        s=str(num)
        
        for c in s:
            if c!='9':
                smax=s.replace(c,'9')
                break
        else:
            smax=s
        for x in s:
            if x!='0':
                smin=s.replace(x,'0')
                break
        else:
            smin=s
        return int(smax)-int(smin)







        # num=list(str(num))
        # i=num[0]
        # maxx=0
        # minn=0
        # for x in range(len(num)):
        #     if 9 !=num[x]:
        #         num[x]='9'
        #     maxx+=num[x]
        # for x in range(len(num)):
        #     if num[x]!=0 :
        #         num[x]='0'
        #     minn+=num[x]
        # a=maxx-minn
        # return a




        
            
        