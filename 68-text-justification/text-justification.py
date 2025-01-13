class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        
        def getWords(i):
            curr_len = 0
            line = []
            while i < len(words) and curr_len + len(words[i]) <= maxWidth:
                curr_len += len(words[i]) + 1
                line.append(words[i])
                i+=1
            return line

        def justify(line,i):
            len_of_line = -1
            for j in range(len(line)):
                len_of_line+= len(line[j]) + 1

            total_spaces = maxWidth - len_of_line
            if len(line)==1 or i==len(words):
                return " ".join(line) + " " * total_spaces
            
            num_of_words = len(line) - 1
            space_per_word = total_spaces // num_of_words
            uneven_space = total_spaces % num_of_words

            # pad uneven
            for j in range(uneven_space):
                line[j]+= " "

            # pad extra besides + 1 we counted
            for j in range(num_of_words):
                line[j]+= " " * space_per_word
            
            # remember 1 we kept counting ? add that
            return " ".join(line)

        ans = []
        i = 0 
        while i < len(words):
            line = getWords(i)
            i+= len(line)
            # print(line, i)
            ans.append(justify(line,i))
        return ans 

        # def getWords(i):
        #     curr_len = 0
        #     line = []
        #     while i < len(words) and curr_len + len(words[i]) <= maxWidth:
        #         line.append(words[i])
        #         curr_len += len(words[i]) + 1
        #         i+=1
        #     return line
        
        # def justify(line):
        #     base_len = -1
        #     for j in range(len(line)):
        #         base_len += len(line[j])+1
        #     # total len of line without " " trailing

        #     total_spaces = maxWidth - base_len
       
        #     num_words = len(line) - 1

          
        #     if len(line)==1 or i == len(words):
        #         return " ".join(line) + " " * total_spaces
        #     spaces_per_word = total_spaces // num_words
        #     remaining_space = total_spaces % num_words

        #     # remaining spaces start adding for leftmost word
        #     for j in range(remaining_space):
        #         line[j]+= " "
            
        #     # distribute evenly 
        #     for j in range(len(line)-1): #num_words
        #         line[j] += " " * spaces_per_word
            

        #     return " ".join(line)



        # ans = []
        # i = 0 
        # while i < len(words):
        #     line = getWords(i) 
        #     #starting at index "i", how many words can you get?
        #     i+= len(line) # number of words
        #     ans.append(justify(line)) 
        # return ans
        #     # if its the last line/ single word, left justfify/
        #     # need something to check

       