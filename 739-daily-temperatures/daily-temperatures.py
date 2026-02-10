class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        Answer = [0]*len(temperatures) 
        Stack = []
        for i, values in enumerate(temperatures):
            if len(Stack) == 0:
                Stack.append(i)
            if temperatures[Stack[-1]] >= temperatures[i]:
                Stack.append(i)
            else:
                while len(Stack) > 0 and temperatures[i] > temperatures[Stack[-1]]:
                    Answer[Stack[-1]] = i - Stack[-1]
                    Stack.pop()
                Stack.append(i)
        return Answer
                    