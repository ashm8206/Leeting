from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        
        # # 1. build hash map : character and how often it appears
        # # O(N) time
        # count = Counter(nums)   
        # # 2-3. build heap of top k frequent elements and
        # # convert it into an output array
        # # O(N log k) time
        # 1: 3
        # 2: 2
        # 3: 1

        # count = Counter(nums) #--> O(n)
        # pq = []

        # for key, value in count.items(): 
        #     heapq.heappush(pq,(value,key))
            
        #     if len(pq) > k:
        #         heapq.heappop(pq)
        
        
        # return [val[1] for val in pq]


        # BUKCET SORT

        bucket = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums).items()  
        for num, freq in count: 
            bucket[freq].append(num) 
        
        flat_list = []
        for sublist in bucket:
            flat_list.extend(sublist)

        return flat_list[::-1][:k]


        if k == len(nums):
            return nums

        c = collections.Counter(nums)
        d = [(c[key],key)for key in c]

        def partition(d, l, r, pivot_index):
            # move pivot index to the end
            d[r], d[pivot_index] = d[pivot_index], d[r]
            
            pivot = d[r]
            
            next_idx = l

            for i in range(l,r):
                if d[i][0] < pivot[0]:
                    d[i], d[next_idx] = d[next_idx], d[i]
                    next_idx+=1
            d[r], d[next_idx] = d[next_idx], d[r]

            return next_idx

        def quickSelect(d, l, r, k):
            if l == r:
                return l

            pivot_index = random.randint(l, r)   

            p = partition(d, l, r, pivot_index)

            if p < k:
                return quickSelect(d, p+1, r, k)
            elif p > k:
                return quickSelect(d, l, p-1, k)
            else:
                return p

        # since we are subtracting len(nums)-k, the correct adjust p is found

        return [ele[1] for ele in d[quickSelect(d, 0, len(d)-1, len(d)-k):]]



       



        