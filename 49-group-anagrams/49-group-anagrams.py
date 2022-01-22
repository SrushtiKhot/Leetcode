class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count={}       
        for words in strs:
            sortedword=''.join(sorted(words))
            if sortedword not in count:
                count[sortedword]=[words]
            else:
                count[sortedword].append(words)             
        return count.values()
            