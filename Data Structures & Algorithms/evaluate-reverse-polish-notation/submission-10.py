class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashmap=set(["+","-","/","*"])
        hash_res=[]
        res=0
        for i in range(len(tokens)):
            if tokens[i] in hashmap:
                match tokens[i]:
                    case "+":
                        res=int(hash_res[-2]) + int(hash_res[-1])
                        hash_res.pop()
                        hash_res.pop()
                        hash_res.append(res)
                    case "-":
                        res=int(hash_res[-2]) - int(hash_res[-1])
                        hash_res.pop()
                        hash_res.pop()
                        hash_res.append(res)
                        
                    case "*":
                        res=int(hash_res[-2]) * int(hash_res[-1])
                        hash_res.pop()
                        hash_res.pop()
                        hash_res.append(res)
                    case "/":
                        res=int(int(hash_res[-2]) / int(hash_res[-1]))
                        hash_res.pop()
                        hash_res.pop()
                        hash_res.append(res)
                        
            else:
                hash_res.append(tokens[i])        
        return int(hash_res[0])