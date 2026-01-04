from collections import defaultdict, Counter
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
        hashmap = Counter(changed)

        for num in changed:
            if hashmap.get(num) > 0:
                hashmap[num] -= 1
                # decrementing first handles the 0 case

                # always check count > 0 leaves no reason to del
                twice = num * 2
                if (hashmap.get(twice) and hashmap.get(twice) > 0):
                    hashmap[twice] -= 1
                    arr.append(num)
                else:
                    return []
        return arr


        # hashMap = defaultdict(list)

        # for i, val in enumerate(changed):
        #     hashMap[val].append(i)


        # for  i, num in enumerate(changed):
        #     if num < 0:
        #         continue
            
        #     double = num*2

        #     if double in hashMap:
        #         if double == 0:
        #             hashMap[double].remove(i) # index of 0
        #             if len(hashMap[double])==0:
        #                 continue

                
        #         changed[hashMap[double][0]] = -1 
        #         # mark pair as used dont use in iteration
        #         hashMap[double].pop(0) 
        #         if len(hashMap[double]) == 0:
        #             del hashMap[double]
        #         # remove its index from list

        #         arr.append(num)

        # return arr if len(arr)==half else []

       
    

       
