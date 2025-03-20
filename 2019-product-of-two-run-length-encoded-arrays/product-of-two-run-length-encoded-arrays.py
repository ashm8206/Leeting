class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        i, j = 0, 0
        res = []
        while i < len(encoded1) and j < len(encoded2):
            product = encoded1[i][0] * encoded2[j][0]
            length = min(encoded1[i][1], encoded2[j][1])
            if res and res[-1][0] == product:
                res[-1][1] += length
            else:
                res.append([product, length])
            encoded1[i][1] -= length
            encoded2[j][1] -= length
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1
        return res

        # def decode(nums):
        #     res = []
        #     for val, freq in nums:
        #         temp = [val] * freq
        #         res.extend(temp)
        #     return res
        
        # def encode(nums):
        #     l = 0
        #     n = len(nums)
        #     res = []
        #     for r in range(n):
        #         if nums[l]!=nums[r]:
        #             res.append([nums[l], r-l])
        #             l = r
        #     res.append([nums[l], r-l+1])
        #     return res
        
        # decoded1 = decode(encoded1)
        # decoded2 = decode(encoded2)

        # # print(decoded1)
        # # print(decoded2)

        # prod = []
        # for num1, num2 in zip(decoded1,decoded2):
        #     prod.append(num1*num2)
        # result = encode(prod)
        # return result

        