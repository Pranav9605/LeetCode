class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        sum=0
        for x in operations:
            if x=='--X' or x=='X--':
                sum-=1
            if x=='X++' or x=='++X':
                sum+=1
        return sum
        
        