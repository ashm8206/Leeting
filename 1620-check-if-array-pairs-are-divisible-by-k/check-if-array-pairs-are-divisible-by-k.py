class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem_count = defaultdict(int)

        for i in arr:
            key = (i%k+k)%k
            # ^ added + k  to keep positive mods
            
            # (ai%k + aj%k)%k= 0
            # 1: ai%k == aj%k = 0
            # 2: ai%k == k - aj%k 

            rem = (k-key)%k
            # ^^ covers both cases
            if rem in rem_count:
                rem_count[rem]-=1
                if rem_count[rem]==0:
                    del rem_count[rem]
                    # pair made, delete
            else:
                rem_count[key]=rem_count.get(key, 0)+1
        return rem_count=={}
            


        # for i in arr:
        #     key = (i%k + k)%k
        #     rem_count[key]+=1
        
        # for i in arr:
        #     rem = (i % k + k) % k

        #     if rem==0:
        #         if rem_count[rem] % 2 == 1:
        #             return False
        #     elif rem_count[rem]!= rem_count[k-rem]:
        #         return False
        # return True