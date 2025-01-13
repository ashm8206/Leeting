class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def getWords(i):
            curr_len = 0
            line = []
            while i < len(words) and curr_len + len(words[i]) <= maxWidth:
                line.append(words[i])
                curr_len += len(words[i]) + 1
                i+=1
            return line
        
        def justify(line):
            base_len = -1
            for j in range(len(line)):
                base_len += len(line[j])+1
            # total len of line without " " trailing

            total_spaces = maxWidth - base_len
       
            num_words = len(line) - 1

          
            if len(line)==1 or i == len(words):
                return " ".join(line) + " " * total_spaces
            spaces_per_word = total_spaces // num_words
            remaining_space = total_spaces % num_words

            # print(total_spaces, base_len, line)
            # print("space/word: ",spaces_per_word )
            # print("remaining_space ",remaining_space )

            result = []
            # remaining spaces start adding for leftmost word
            for j in range(remaining_space):
                line[j]+= " "
            
            # distribute evenly 
            for j in range(len(line)-1): #num_words
                line[j] += " " * spaces_per_word
            

            return " ".join(line)



        ans = []
        i = 0 
        while i < len(words):
            line = getWords(i) 
            #starting at index "i", how many words can you get?
            i+= len(line) # number of words
            ans.append(justify(line)) 
        return ans
            # if its the last line/ single word, left justfify/
            # need something to check

        # def get_words(i):
        #     current_line = []
        #     curr_length = 0

        #     while i < len(words) and curr_length + len(words[i]) <= maxWidth:
        #         current_line.append(words[i])
        #         curr_length += len(words[i]) + 1
        #         i += 1

        #     return current_line

        # def create_line(line, i):
        #     base_length = -1
        #     for word in line:
        #         base_length += len(word) + 1

        #     extra_spaces = maxWidth - base_length

        #     if len(line) == 1 or i == len(words):
        #         return " ".join(line) + " " * extra_spaces

        #     word_count = len(line) - 1
        #     spaces_per_word = extra_spaces // word_count
        #     needs_extra_space = extra_spaces % word_count

        #     for j in range(needs_extra_space):
        #         line[j] += " "

        #     for j in range(word_count):
        #         line[j] += " " * spaces_per_word

        #     return " ".join(line)

        # ans = []
        # i = 0

        # while i < len(words):
        #     current_line = get_words(i)
        #     i += len(current_line)
        #     ans.append(create_line(current_line, i))

        # return ans