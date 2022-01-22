class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        count={}       
        for words in strs:
            sortedword=''.join(sorted(words))
            if sortedword not in count:
                count[sortedword]=[words]
            else:
                count[sortedword].append(words)             
        return count.values()
    #O(m*nlogn) Time complexity
    #O(n*k) n is length of one word in strs k is len(strs)
'''
        res=defaultdict(list)
        #create count for every word in strs
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1                
            res[tuple(count)].append(s)             
        return res.values()
                
        
    
    
            