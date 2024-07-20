from collections import deque
from sortedcontainers import SortedList

# LinkedList / Array 

# Arrays
# get O(1)
# Fetch in O(n) as you gotta move N elements

# Doubly Linked, (Pop in the Middle),  Doubly works better as we need the pointer to the element before
# get O(n)
# fetch O(1)

# TreeSet, AVL Tree SortedList 
# What is AVL, How does Self-balancing Work
# log(n) < SQRT(N)
class MRUQueue:

    def __init__(self, n: int):
        # Method II SortedList 
        # self.q = SortedList([ (i, i) for i in range(1, n+1)])
        # Stored as Index, Value, sorted on Index

        # Method III sqrt(n) 
        nums = list(range(1, n + 1))
        self.buckets = []

        self.sqrt = math.floor(math.sqrt(n))
        # why Ceil ? 
        # It should work with floor too, 
        # but it will mean more buckets ans bukcet_size is small

        # Steps are:
        #    # 1: get and pop -> indexing O(1) 
        #        for bucket first,  k-1//Sqrt -> How many Times?
        #        then into bucket for idx.  k-1%Sqrt  
        #                  this SQRT get very 
        #                  imp while finding th exact element idx inside bucket
        #    # 2: append ->  to the last bucket O(1)
        #    # adjust buckets from bucket[candidate_found] ---> bucket[Last]
        #     Move leftmost from any bucket to right of candidate bucket, 
        #     1 bucket down
        #     Repeat and TC - (n^1/2)

        for i in range(0, n, self.sqrt):
            chunk = nums[i: i+self.sqrt]
            self.buckets.append(chunk)

        self.len_of_buckets = len(self.buckets)
        # print(self.buckets)


    def fetch(self, k: int) -> int:

        # SortedList from sortedcontainers (works with Map, Dict APIs )
        # O(log(n))
        # last_idx = self.q[-1][0] # Pops from an empty list
        # _ , value  = self.q.pop(k-1) # 1 indexed, make it 0
        # self.q.add((last_idx+1, value)) 

        # return value

        # Method III SQRT

        bucket_idx = (k-1) // self.sqrt # Quotient
        element_idx = (k-1) % self.sqrt # Remainder how many deviations within bucket
        # Get and Del
        element = self.buckets[bucket_idx].pop(element_idx)

        # append to the end of last bucket
        self.buckets[self.len_of_buckets - 1].append(element)

        # Adjust buckets [cand_bucket]--- > [last_bucket but 1 bucket] 
        #  more their 1st idx to bucket before it

        for b in range(bucket_idx, self.len_of_buckets - 1):
            left_bucket = self.buckets[b]
            right_bucket = self.buckets[b+1]

            left_bucket.append(right_bucket.pop(0))

        return element



# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)