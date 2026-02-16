class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        stack = []

        dictionary = {}
        for i in range(len(position)):
            dictionary[position[i]] = speed[i]
        position.sort()
        for i in position[::-1]:
            print(i)
            distance = target - i
            speed = dictionary[i]
            time = float(distance)/speed
            print(time)
            if len(stack) == 0:
                stack.append(time)
            else:
                if stack[-1] < time:
                    stack.append(time)
        return len(stack)