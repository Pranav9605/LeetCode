class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out=[]
        lens=len(nums)//2
        for x in range (lens):
            out.append(nums[x])
            out.append(nums[x+n])
            print(out)
        return out        