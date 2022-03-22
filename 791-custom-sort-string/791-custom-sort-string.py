class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #Counter to store occurances of chars in order
        count=collections.Counter(s)
  
        res=[]
        
        for c in order:
            res.append(c*count[c])
            count[c]=0
            
        for c in count:
            res.append(c*count[c])
            
        return ''.join(res)
            
            
        
        