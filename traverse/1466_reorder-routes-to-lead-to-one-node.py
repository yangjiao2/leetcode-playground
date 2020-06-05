# Reorder Routes to Make All Paths Lead to the City Zero
# Add to List

# Share
# There are n cities numbered from 0 to n-1 and n-1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [a, b] represents a road from city a to b.
# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.
# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
# It's guaranteed that each city can reach the city 0 after reorder.


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0    
		roads = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)
        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)    
        dfs(0, -1)
        return self.res
                    