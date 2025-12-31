class Solution(object):
    def frogPosition(self, n, edges, t, target):
        from collections import defaultdict
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()
        def dfs(node, time, prob):
            visited.add(node)
            
            if time == t:
                return prob if node == target else 0

            choices = 0
            for nei in graph[node]:
                if nei not in visited:
                    choices += 1
            
            if node == target:
                return prob if choices == 0 else 0

            if choices == 0:
                return 0

            ans = 0
            for nei in graph[node]:            
                if nei not in visited:
                    ans = ans + dfs(nei, time+1, prob/choices)
            return ans
        return dfs(1, 0, 1.0)
