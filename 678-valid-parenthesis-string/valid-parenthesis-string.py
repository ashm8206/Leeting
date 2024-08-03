class Solution:
    def checkValidString(self, s: str) -> bool:

        openstack = []
        asterisk = []

        for i, ch in enumerate(s):
            if ch=='(':
                openstack.append(i)
            elif ch=='*':
                asterisk.append(i)
            else:

                if openstack:
                    openstack.pop()
                elif asterisk:
                    asterisk.pop()
                    # asterisk idx that came before this ')'
                    # asterisk can substiture open bracket
                else:
                    return False
    
        while openstack and asterisk:
            if openstack[-1] > asterisk[-1]:
                # if open bracket came after close bracket
                #  we cant substitute asterisk as "close bracket"
                 return False
            else:
                openstack.pop() 
                asterisk.pop()
        
        return len(openstack)==0
