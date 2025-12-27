class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        INF = 1e9 + 7
        distanceMatrix = [[INF]*n for i in range(n)]
        for i in range(n):
            distanceMatrix[i][i] = 0
        for start, end, weight in edges:
            distanceMatrix[start][end] = weight
            distanceMatrix[end][start] = weight
        self.floyd(n, distanceMatrix)
        return self.getCityWithFewestReachable(n, distanceMatrix, distanceThreshold)
    def floyd(self, n, distanceMatrix):
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distanceMatrix[i][j] =min(
                        distanceMatrix[i][j], distanceMatrix[i][k] + distanceMatrix[k][j]
                    )
    def getCityWithFewestReachable(self, n, distanceMatrix, distanceThreshold):
        LowestCountTillNow = n
        countForThisCity = -1
        for i in range(n):
            countForThisCity = 0
            for j in range(n):
                if i != j and distanceMatrix[i][j] <= distanceThreshold:
                    countForThisCity += 1
            if countForThisCity <= LowestCountTillNow:
                LowestCountTillNow = countForThisCity
                CityWithFewestReachable = i
        return CityWithFewestReachable