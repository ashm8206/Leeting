class Solution:
    def confusingNumber(self, n: int) -> bool:

        invert_map = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}

        rotated_num = []

        for ch in str(n):
            if ch not in invert_map:
                return False # rotation becomes invalid

            rotated_num.append(invert_map[ch])

        rotated_num = "".join(rotated_num)



        return int(rotated_num[::-1])!=n
            

        
