class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Can you find the Number of Unbalanced parenthesis and return that?
        
        openstack = []
        unbalanced = 0
        for ch in s:
            if ch == '(':
                openstack.append('(')
            else:
                "Encountered a close, can we balance it ?"
                if openstack:
                    openstack.pop()
                else:
                    unbalanced +=1

        return len(openstack) + unbalanced

        # return unbalanced open parenthesis from Openstack  + Unbalanced pair counts

    