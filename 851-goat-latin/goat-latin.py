class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        res = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        for i, word in enumerate(sentence.split(" "), 1):
            # if word ==" " or not word:
            #     continue

            if word[0] in vowels:
                res.append(word + "ma" + i*"a")
            else:
                res.append(word[1:] + word[0] + "ma" + i*"a")
        return " ".join(res)
            