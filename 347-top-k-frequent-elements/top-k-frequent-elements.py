class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mp = {}
        Output = []
        for i in nums:
            mp[i] = mp.get(i,0) + 1
        while k > 0:
            Current_Greatest_mp_value = 0
            for i in mp:
                if mp[i] > Current_Greatest_mp_value:
                    Current_Greatest_mp_value = mp[i]
            for i in mp:
                if mp[i] == Current_Greatest_mp_value:
                    Output.append(i)   
                    mp[i] = 0
                    break
            k = k-1
        return Output

        
        