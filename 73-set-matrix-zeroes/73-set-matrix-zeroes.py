class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])  
        rowzero=False   
        
        #First loop for identofying 0's in matrix
        
        for r in range(row): 
            for c in range(col):
                if matrix[r][c]==0: #If you encounter 0 
                    matrix[0][c]=0 #Mark that the column needs to be changed to 0
                    
                    #r=0 is handled by a dedicated rowzero value inorder to avoid overlapping
                    
                    if(r>0): 
                        matrix[r][0]=0 
                    else:
                        rowzero=True   
                        
        #Second loop to check which row and column needs to made 0
        #We won't be considering the matrix[0][0] as it changes the further values that we want to traverse
        
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0 #Make present cell as 0
                    
                    
        if matrix[0][0]==0: #0th column to be made 0
            for r in range(row):
                matrix[r][0]=0
                
        if rowzero: #0th row to be made 0
            for c in range((col)):
                matrix[0][c]=0
                
        
                    
        
                        
                    
                    
        
        