class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return[b for a,b in sorted(zip(heights,names),reverse=True)]










        # user = dict(zip(heights,names))
        # tallest = sorted(user.keys(),reverse=True)
        # ans=[user[height] for height in tallest]
        # return ans

        