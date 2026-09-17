class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]       

    def push(self, val: int) -> None:
        self.stack.append(val)        
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(self.min_stack[-1],val))
    """
    optimized push function
    def push(self, val: int) -> None:
        if not stack:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(min_stack[-1], val))
            self.stack.append(val)
    """
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        #could also use slicing [:-1], but makes compy of that stack

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
