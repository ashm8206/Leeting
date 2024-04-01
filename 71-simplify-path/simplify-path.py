class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        directories = path.split("/")

        for directory in directories:
            if directory == '' or directory =='.':
                continue
            elif directory=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        print(directories)
        return "/"+ "/".join(stack)
        

        """"
        Input: "/a//b//c//////d"
        OP: "/a/b/c/d"

        "/home/user/./Downloads/../Pictures/././"
        "/home/user/Pictures"

        "/../"
        "/"
        --> Split  : ['', '..', '']
        """