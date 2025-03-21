class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        directories = path.split("/")
        # # This deals with the multiple lash problem
        # # split on '/' we are dealing only with directory names

        # print(directories)
        for dr in directories:
            if dr == '.' or dr=='':
                continue
            elif dr == '..':
                if stack:
                    stack.pop()

            else:
                # "..." is valid
                # any directory name
                stack.append(dr)
        
        return "/" +  "/".join(stack)

        

        # """"
        # Input: "/a//b//c//////d"
        # OP: "/a/b/c/d"

        # "/home/user/./Downloads/../Pictures/././"
        # "/home/user/Pictures"

        # "/../"
        # "/"
        # --> Split  : ['', '..', '']
        # """

       
        
        print(directorties)
        for dr in directorties:
            if dr == '..':
                if stack:
                    stack.pop()
                else:
                    # if stack is empty and you cant pop, you have reached the root
                    return '/'
            elif dr == '.' or dr=='':
                continue
            else:
                # "..." is valid
                # any directory name
                stack.append(dr)
        
        return "/" +  "/".join(stack)

        # Join works by adding "-" or " " between two values of iterable
            
            
