class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        mp = defaultdict(list)
        for word in strs:
            our_list = [0]*26
            for letter in word:
                our_list[ord(letter)-ord("a")] += 1
            mp[tuple(our_list)].append(word)            
        return list(mp.values())