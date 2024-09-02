class Solution:
    def countOfAtoms(self, formula: str) -> str:
        multiplier_stack = []
        atom = ''
        count = ''
        running_multiplier = 1
        hmap = {}
        


        # for ch in formula[::-1]:

        #     if ch.isalpha():

        #         if ch.isupper():
        #             atom = ch + atom 
        #             if count: 
        #                 count = int(count) * running_multiplier
        #             else:
        #                 count = 1 * running_multiplier
        #             hmap[atom] = hmap.get(atom, 0) + count

        #             count = ''
        #             atom = ''
        #         if ch.islower():
        #             atom = ch + atom
        #     elif ch.isdigit():
        #         count = ch + count

        #     elif ch is ')':
        #         curr_multiplier = int(count) if count else 1
        #         multiplier_stack.append(curr_multiplier)
        #         running_multiplier *= curr_multiplier
        #         count = ""

        #     elif ch == '(':
        #         # reset it 
        #         running_multiplier //= multiplier_stack.pop()
        
        # return "".join([ key + str(value) if value > 1 else key for key, value in sorted(hmap.items()) ])

        for ch in formula[::-1]:
            if ch.isalpha():
                if ch.isupper():
                    atom = ch + atom  # pre-pend the Upper it
                    # we hit the boundary condition for starting new atom
                    # add the atom in Map
                    if count: 
                        count = int(count) * running_multiplier
                    else:
                        count = 1 * running_multiplier
                    hmap[atom] = hmap.get(atom, 0) + count

                    atom = ''
                    count = ''
                if ch.islower():
                    atom = ch + atom
        
            elif ch.isdigit():
                count = ch + count

            elif ch == ')':
                curr_multiplier = int(count) if count else 1
                multiplier_stack.append(curr_multiplier)
                running_multiplier *= curr_multiplier
                count = ""
            elif ch == '(':
                running_multiplier //= multiplier_stack.pop()

        smap =[ k + str(v) if v > 1 else k for k, v in sorted(hmap.items(), key = lambda k : k[0])]
        print(smap)
        return "".join(smap)