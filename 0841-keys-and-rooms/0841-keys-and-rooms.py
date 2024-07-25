class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        path = defaultdict(list)
        
        for i, key in enumerate(rooms):
            for k in key:
                path[i].append(k)
            
        visited = set()
        
        def dfs(room):
            if room in visited:
                return
            
            visited.add(room)
            
            for j in path[room]:
                dfs(j)
                
        
        dfs(0)
        
        return len(visited) == len(rooms) 