class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l,r=0,len(matrix)-1
        t,b=l,r

        while(l<r):
            for i in range(r-l):
                topleft=matrix[t][l+i]
                matrix[t][l+i]=matrix[b-i][l]
                matrix[b-i][l]=matrix[b][r-i]
                matrix[b][r-i]=matrix[t+i][r]
                matrix[t+i][r]=topleft
                
            r-=1
            l+=1
            t+=1
            b-=1



        
        
        
        