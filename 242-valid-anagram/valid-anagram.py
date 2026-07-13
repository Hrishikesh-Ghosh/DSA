class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Map = {}
        for i in s:
            Map[i] = Map.get(i,0) + 1
        for i in t:
            Map[i] = Map.get(i,0) - 1
        for i in Map:
            if Map[i] == 0:
                continue
            else:
                return False
        return True
        