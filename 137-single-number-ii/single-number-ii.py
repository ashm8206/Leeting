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
            # 3rd Appearance: Becuase in seenTwice, don't add to seenOnce

            seen_once = ~seen_twice & (seen_once ^ num)
            # seen Once and Only once and NOT in seenTwice
            
           
            # & ~SeenOnce
            # If a bit in num is also in seenOnce, 
            # the AND operation will ensure that the number does not get added to seenTwice

            # This ensures only those seenTwice are added in SeenTwice
            # As double numbers will Null out in seenOnce.
            
            seen_twice = ~seen_once & (seen_twice ^ num)
            #^ Not in seenOnce but in SeenTwice
        return seen_once



        