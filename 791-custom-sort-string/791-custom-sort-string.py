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
    
    #O(len(order)+len(s)) as we traverse through both the strings
    #O(len(s)) As we store counter of all the elemenets present in s
            
            
        
        