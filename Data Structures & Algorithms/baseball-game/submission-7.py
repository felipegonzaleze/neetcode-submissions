class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        res = 0
        for o in operations:
            match o:
                case '+':
                    res += record[-1]+record[-2]
                    record.append(record[-1]+record[-2])
                case 'D':
                    res += record[-1]*2
                    record.append(record[-1]*2)
                case 'C':
                    res -= record[-1]
                    record.pop()
                case _:
                    record.append(int(o))
                    res += int(o)
        return res