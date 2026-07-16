class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Ans = []
        Hmap = {}
        for i in nums:
            Hmap[i] = Hmap.get(i,0) + 1

        while k>0:
            GreatestHmapElement = 0
            for i in Hmap:
                if Hmap[i] > GreatestHmapElement:
                    GreatestHmapElement = Hmap[i]
            for i in Hmap:
                if Hmap[i] == GreatestHmapElement:
                    Ans.append(i)
                    Hmap[i] = 0
                    break 
            k-=1

        return Ans