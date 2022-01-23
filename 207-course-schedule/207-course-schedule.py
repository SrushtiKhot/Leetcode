class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #We use hashmap to keep courses as keys and it's prerequisites as values
        
        premap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:  #premap created
            premap[crs].append(pre)
        visit=set()   #Set to keep track which course is already taken
        def dfs(crs):
            if crs in visit: #There exists a loop
                return False
            if premap[crs]==[]: #If no prereq required to complete crs
                return True
            visit.add(crs)  #Mark course as visited
            for pre in premap[crs]: #Run dfs on all prereq of course
                if not dfs(pre): #If a single prereq of crs returs false,return false
                    return False
            visit.remove(crs)   
            premap[crs]=[]  #If dfs is true delete the prereq of course
            return True
    
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
    
    #O(n+m) n is numCourses and m is prerequistes Time complexity
    