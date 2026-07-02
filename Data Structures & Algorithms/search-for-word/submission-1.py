class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
         ROWS, COLS = len(board),len(board[0])
         path = set()


         def dfs(r,c,idx):
             #iterate through the board
             if idx == len(word): #we have reached last position/ length of word
                     return True # base case
             #out of bounds
             if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[idx] != board[r][c] or (r,c) in path):
                 return False
             
             path.add((r,c))
             #look at every possible adjacent position
             res = (dfs(r+1,c,idx+1) or 
                    dfs(r-1,c,idx+1) or 
                    dfs(r,c+1,idx+1) or 
                    dfs(r,c-1,idx+1))
             path.remove((r,c)) #no longer in our path of interest since everything is unique
             return res
         for i in range(ROWS):
            for j in range(COLS):
                 if dfs(i,j,0):
                     return True
         return False


                

             




             







         

