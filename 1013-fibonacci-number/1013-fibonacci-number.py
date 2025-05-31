class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        prev=0
        curr=1
        for x in range(2,n+1):
            prev,curr=curr,prev+curr
        return curr








        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)



        