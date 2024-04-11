class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = []

        for word in title.split(" "):
            
            if len(word)<=2:
                word = word.lower()
            else:
                word = word.capitalize()
            res.append(word)

        return " ".join(res) 
