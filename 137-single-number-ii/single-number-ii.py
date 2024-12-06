class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #  Mod 3 logic
        # Seen zero = 0 / 3
        # Seen once == what interest is
        # Seen twice == we expect a 3rd and this are not the bit of the ans

        seen_once = seen_twice = 0

        """Algo:
        1. Add to seenOnce when a number appears for the first time.
        2. Move from seenOnce to seenTwice when a number appears for the second time.
        3.Remove from seenTwice when a number appears for the third time."""
        
        for num in nums:

           
            # XOR with Seen_Once
            # If num was seen once before, it will be removed from seenOnce  
            # If not, then it will be added to seenOnce.

            # & with !seenTwice: 
            # Any num in seenOnce also in seenTwice are removed from seenOnce
            seen_once = ~seen_twice & (seen_once ^ num)
            
            # XOR with Seen_Twice
            # If num was seen twice/even times before, it will be added
            # If seen odd times it will be removed, 

            # & with !seenOnce: 
            #  ~seenOnce masks out bits that are already set in seenOnce. 
            # If a bit in num is also in seenOnce, 
            # the AND operation will ensure that the number does not get added to seenTwice again.

            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once



        