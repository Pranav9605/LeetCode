class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for x in range(len(arr)-2):
            if arr[x]%2==1 and arr[x+1]%2==1 and arr[x+2]%2==1:
                return True

        return False

        