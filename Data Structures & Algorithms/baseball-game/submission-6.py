class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for i in range (len(operations)):
            if operations[i] == '+':
                score1 = points.pop()
                score2 = points[-1]
                total = int(score1 + score2)
                points.append(score1)
                points.append(total)
            elif operations[i] == 'D':
                score = points[-1]
                total = int(score * 2)
                points.append(total)
            elif operations[i] == 'C':
                points.pop()
            else:
                points.append(int(operations[i]))
        return sum(points)
                



        