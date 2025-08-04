class Solution:
    def isValid(self, word: str) -> bool:
        vow=['a', 'e', 'i', 'o', 'u']
        vow_count=0
        cons_count=0
        if len(word)<3:
            return False
        for x in word.lower():
            if x.isdigit():
                continue
            elif x.isalpha():
                if x in vow:
                    vow_count+=1
                else:
                    cons_count+=1
            else:
                return False
        return vow_count >0 and cons_count>0


        



        