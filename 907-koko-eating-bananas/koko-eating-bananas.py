class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while (l<=r): 
            hours = 0
            m = (l+r)//2
            for i in piles:
                hours += math.ceil(i/m)
            if hours <= h:
                r = m-1
            else:
                l = m+1
        return l