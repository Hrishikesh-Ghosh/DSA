class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mp = {}
        for i in s:
            mp[i] = mp.get(i,0) + 1
        print (mp)
        for i in t:
            mp[i] = mp.get(i,0) - 1
        print (mp)
        for i in mp:
            if mp[i] == 0:
                continue
            else:
                return False
        return True