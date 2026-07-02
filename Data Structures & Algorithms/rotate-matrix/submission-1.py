class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
         #make horiz vertical
         matrix.reverse()

         #transpose matrix
     
         for i in range(len(matrix)):
            for j in range(i + 1,len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        



