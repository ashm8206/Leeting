class TrieNode:
    def __init__(self, value = ""):
        self.children = dict()
        self.content = value
        self.is_dir = False

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        

    def ls(self, path: str) -> List[str]:
    
        node = self.root
        if path!="/":
            folders = path.split("/")
            for i, f in enumerate(folders):
                if f == "":
                    continue
                node = node.children[f] # keep going down
        # return  else:
            if not node.is_dir:
                return [f] # return a list that contains this files name
        return [k for k, v in sorted(node.children.items())]

    def mkdir(self, path: str) -> None:
        node = self.root
        folders = path.split("/")

        for i, f in enumerate(folders):
            if f == "":
                continue
        
            if f not in node.children:
                node.children[f] = TrieNode()
            node = node.children[f] # if it exists move or move after creation
            node.is_dir = True

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        folders = filePath.split("/")

        for i, f in enumerate(folders):
            if f == "":
                continue
        
            if f not in node.children:
                node.children[f] = TrieNode()
            node = node.children[f] # if it exists move or move after creation
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        folders = filePath.split("/")
      
        for i, f in enumerate(folders):
            if f == "":
                continue
            node = node.children[f] # if it exists move or move after creation
        return node.content



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)