class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        

        def helper(expression):
            result = []

            if len(expression) == 0:
                return result # empty list

            
            if len(expression) <= 2 :
                return [int(expression)]

            # if len(expression) == 1:
            #     return [int(expression)]
            
            # if len(expression) == 2 and expression[0].isdigit():
            #     return [int(expression)]
            

            for i, ch in enumerate(expression):

                if ch.isdigit():
                    continue
                
                left = helper(expression[:i])
                right = helper(expression[i+1:])

                for left_val in left:
                    for right_val in right:
                        if ch =="+":
                            result.append(left_val+right_val)
                        
                        elif ch =="-":
                            result.append(left_val-right_val)
                        
                        else:
                            result.append(left_val*right_val)
            return result
                       
        return helper(expression)