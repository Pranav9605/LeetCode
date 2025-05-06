class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        out=[]
        for x in range (len(number)):
            if number[x]==digit:
                out.append(number[:x]+number[x+1:])
        return max(out)


        