class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        ls_words = [ word for word in s.split(" ") if len(word)>0==False]
        res =[]
        while ls_words:
            res.append(ls_words.pop())
        
        return " ".join(res)
        


        