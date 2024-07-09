class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        connect = defaultdict(list)
        indegree = [0] * numCourses
        
        for i, j in prerequisites:
            connect[j].append(i)
            indegree[i] += 1
            
            
        
        q = deque()
        
        for k, v in enumerate(indegree):
            if v == 0:
                q.append(k)
        
        count = 0
        while q:
            count += 1
            course = q.popleft()
            for c in connect[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
                    
                
        return count == numCourses
        