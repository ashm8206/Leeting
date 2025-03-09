class Solution:
    def removeDuplicates(self, s: str) -> str:

        output = []
        for ch in s:
            if output and ch == output[-1]: 
                output.pop()
            else: 
                output.append(ch)
        return ''.join(output)


        # def remove_all_adjacent_duplicates_variant_1047(s):
        #     letters = []
        #      input: azxxxzy
        #      output: ay
        #      a, 1: Loop1
        #      z, 1: Loop4
        #      x: 3: Loop2
        #      z: Loop 4 -->  a: 1, z:2

        #      y: Loop 3 then Loop 4
            
        #     for ch in s:
        #         Loop1:
        #         if not letters:
        #             letters.append([ch, 1])
        #             continue

        #         Loop2:        
        #         if letters[-1][0] == ch:
        #             letters[-1][1] += 1
        #             continue # continue to find more

        #         Loop3:
        #         # at next z pop x
        #         if letters and letters[-1][1] > 1:
        #             letters.pop()
                
        #         Loop4:       
        #         if not letters or letters[-1][0] != ch:
        #             letters.append([ch, 1])
        #         else:
        #             letters[-1][1] += 1
        #     Loop5:
        #     if letters and letters[-1][1] > 1:
        #         letters.pop()

        #     result = ''.join([letter[0] for letter in letters])
        #     return result

        # s = "azxxxzy"
        # print(remove_all_adjacent_duplicates_variant_1047(s))
        # assert("ay" == remove_all_adjacent_duplicates_variant_1047(s))

        # s = "abbaxx"
        # print(remove_all_adjacent_duplicates_variant_1047(s))
        # assert(""==remove_all_adjacent_duplicates_variant_1047(s))

        # s = "aabbccdd"
        # print(remove_all_adjacent_duplicates_variant_1047(s))
        # assert(""==remove_all_adjacent_duplicates_variant_1047(s))

        # s = "aaabbaad"
        # print(remove_all_adjacent_duplicates_variant_1047(s))
        # assert("d" == remove_all_adjacent_duplicates_variant_1047(s))

        