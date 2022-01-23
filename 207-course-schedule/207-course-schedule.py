class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #We use hashmap to keep courses as keys and it's prerequisites as values
        
        premap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:  #premap created
            premap[crs].append(pre)
        visit=set()
        def dfs(crs):
            
            if crs in visit:
                return False
            if premap[crs]==[]:
                return True
            
            visit.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            premap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True