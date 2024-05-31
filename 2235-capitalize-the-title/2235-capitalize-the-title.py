class Solution:
    def capitalizeTitle(self, title: str) -> str:
        a=title.split()
        output=[]
        for x in a:
            if len(x)<=2:
                output.append(x.lower())
            else:
                output.append(x.capitalize())
        return ' '.join(output)
        
        