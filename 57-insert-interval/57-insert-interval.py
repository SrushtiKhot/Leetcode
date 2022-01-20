class Solution:
    def insert(self, intervals: List[List[int]], newinterval: List[int]) -> List[List[int]]:
        #non-ovrelapping
        res=[]
        
        for i in range(len(intervals)):        
            if(newinterval[1]<intervals[i][0]): #if end is small than i's start, no overlapping occurs
                res.append(newinterval) #As new intervals doesnt overlap add to res
                return res+intervals[i:] #As intervals are sorted, if newinterval doesnt overlap with the first element then others remain intact
            elif(newinterval[0]>intervals[i][1]): #If start appears after the end of  interval at i
                res.append(intervals[i])               
            else:
                newinterval=[min(newinterval[0],intervals[i][0]),max(newinterval[1],intervals[i][1])]              
        res.append(newinterval)             
        return res