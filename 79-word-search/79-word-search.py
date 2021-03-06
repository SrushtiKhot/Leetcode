class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        visited=set()
        
        def dfs(r,c,i):
            if(i==len(word)): #i has come to emd of word that means we have found word 
                return True
            
            if(r<0 or c<0 
              or r>=row or c>=col
              or word[i]!=board[r][c]
              or (r,c) in visited):
                return False
            
            visited.add((r,c))  
            res=(dfs(r-1,c,i+1) or
                dfs(r+1,c,i+1) or
                dfs(r,c-1,i+1) or
                dfs(r,c+1,i+1) )
            visited.remove((r,c)) #removing as the r,c shouldn't print the prev value again
                
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0): return True
        return False
        
        
        