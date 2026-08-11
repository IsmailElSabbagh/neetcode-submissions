
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for i in range(len(operations)):
            if operations[i] != '+' and operations[i] != 'D' and operations[i] != 'C':
                record.append(int(operations[i]))
            if operations[i] == '+':
                record.append(record[-1]+record[-2])
            elif operations[i] == 'D':
                record.append(2*record[-1])
            elif operations[i] == 'C':
                del record[-1]
            
        return sum(record)
