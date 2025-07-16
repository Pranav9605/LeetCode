class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        a=0
        for x in fruits:
            for y in range(len(baskets)):
                if x<=baskets[y]:
                    baskets[y]=0
                    break
            else:
                a+=1
        return a



        