class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x: (x[0], x[1]))

        final_list = []
        for i in intervals:
            if not final_list or final_list[-1][1] < i[0]:
                final_list.append(i)
            else:
                final_list[-1][1] = max(final_list[-1][1], i[1]) 

        return final_list