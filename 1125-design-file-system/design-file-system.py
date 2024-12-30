class TrieNode:
        def __init__(self, value = 0):
            self.value = value
            self.children = {}
        
class FileSystem:
    
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:

        node = self.root
        folders = path.split("/")

        for i, f in enumerate(folders):

            if f == "":
                continue
        
            if f not in node.children:
                if i < len(folders) - 1:
                    return False
                else:
                    # last Value
                    node.children[f] = TrieNode(value)
                    return True
            else:
                node = node.children[f]
                # keep  going down
        return False  # if it already exist # return False
    
    def get(self, path: str) -> int:
        folders = path.split("/")
        node = self.root
        for i, f in enumerate(folders):
            if f == "":
                continue

            if f in node.children:
                node = node.children[f]
            else:
                return -1
        return node.value
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)