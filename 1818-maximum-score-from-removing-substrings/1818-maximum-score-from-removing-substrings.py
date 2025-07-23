class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def do(val, tar , s):
            stack = []
            ans = 0
            for c in s:
                if stack and stack[-1] + c == tar:
                    stack.pop()
                    ans += val
                else:
                    stack.append(c)
            return stack , ans
        arr = [(y,"ba"),(x,"ab")]
        arr.sort()
        ans = 0


        firsts , firstv = do(*arr.pop(), s)
        secs , secv = do(*arr.pop(), firsts)
        return max(ans,firstv + secv)
        