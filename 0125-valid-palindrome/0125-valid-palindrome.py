class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=""
        for x in s:
            if x.isalnum():
                c+=x.lower()
        print(x)

        if c==c[::-1]:
            return True
        else:
            return False