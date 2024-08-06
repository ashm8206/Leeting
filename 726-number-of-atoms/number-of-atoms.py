class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        atom = ''
        count = ''
        running_multiplier = 1
        hmap = {}
        


        for ch in formula[::-1]:

            if ch.isalpha():

                if ch.isupper():
                    atom = ch + atom 
                    if count: 
                        count = int(count) * running_multiplier
                    else:
                        count = 1 * running_multiplier
                    hmap[atom] = hmap.get(atom, 0) + count

                    count = ''
                    atom = ''
                if ch.islower():
                    atom = ch + atom
            elif ch.isdigit():
                count = ch + count

            elif ch is ')':
                curr_multiplier = int(count) if count else 1
                stack.append(curr_multiplier)
                running_multiplier *= curr_multiplier
                count = ""

            elif ch == '(':
                # reset it 
                running_multiplier //= stack.pop()
        
        return "".join([ key + str(value) if value > 1 else key for key, value in sorted(hmap.items()) ])

