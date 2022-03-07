from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        remaining=[]
        closest=[]
        
        for p in points:
            dist.append(self.euclidean(p))
            
        for p in range(len(points)):
            remaining.append(p)
            
        low=0
        high=max(dist)
            
        while k:
            mid=(low+high)/2
            
            closer,farther=self.splitlist(remaining,dist,mid)
            if len(closer)>k:
                high=mid
                remaining=closer
                
            else:
                k-=len(closer)
                closest.extend(closer)
                remaining=farther
                low=mid
                
                
        return [points[i] for i in closest]
                
       
    def euclidean(self,point):
        return(pow(point[0],2)+pow(point[1],2))
    
    def splitlist(self,remaining,dist,mid):
        closer=[]
        farther=[]
        for r in remaining:
            if dist[r]<=mid:
                closer.append(r)
            else:
                farther.append(r)
                
        return([closer,farther])
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#         res=sorted(points,key=lambda x:(x[0]*x[0])+x[1]*x[1]) #Sorts points list taking dist as key
#         print(res)
#         return res[:k]
            
        
            
    
            
          
        