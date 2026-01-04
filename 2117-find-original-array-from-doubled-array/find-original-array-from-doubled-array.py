from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # if len(changes) not even return []
        # arr = []
        #  if ele* double exists in set(changed) add this ele to arr
        #  return arr if len(arr)== n/2 else []

        changed.sort()

        n = len(changed)
        half = n // 2

        if n%2==1:
            return []


        arr = []
        hashMap = defaultdict(list)

        for i, val in enumerate(changed):
            hashMap[val].append(i)


        for  i, num in enumerate(changed):
            if num < 0:
                continue
            
            double = num*2

            if double in hashMap:
                if double == 0:
                    hashMap[double].remove(i) # index of 0
                    if len(hashMap[double])==0:
                        break

                
                changed[hashMap[double][0]] = -1 
                # mark pair as used dont use in iteration
                hashMap[double].pop(0) 
                if len(hashMap[double]) == 0:
                    del hashMap[double]
                # remove its index from list

                arr.append(num)

        return arr if len(arr)==half else []

       
    

       
