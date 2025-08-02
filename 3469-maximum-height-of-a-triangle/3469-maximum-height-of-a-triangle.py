class Solution:
    def maxHeightOfTriangle(self, redd: int, bluee: int) -> int:
        def build(yes):
            curr_row=1
            totalrow=0
            red_turn=yes
            red=redd
            blue=bluee
            while True:
                if red_turn is True:
                    if red>= curr_row:
                        red-=curr_row
                    else:
                        break
                else:
                    if blue>=curr_row:
                        blue-=curr_row
                    else:
                        break
                totalrow+=1
                curr_row+=1
                red_turn=not red_turn
            return totalrow
        return max(build(True),build(False))




        