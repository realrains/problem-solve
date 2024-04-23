class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        pathes = [set() for _ in range(len(edges) + 1)]
        vertex = set([i for i in range(len(edges) + 1)])
        
        for s, e in edges:
            pathes[s].add(e)
            pathes[e].add(s)
        
        while len(vertex) > 2:
            dis = set()
            for v in vertex:
                if len(pathes[v]) == 1:
                    dis.add(v)
            
            for v in vertex:
                pathes[v] -= dis

            vertex -= dis
        
        return list(vertex)
