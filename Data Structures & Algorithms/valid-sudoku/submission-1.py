class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRowsCols(board: List[List[str]], isVertical: bool) -> bool:
            i = 0
            while(i < 9):
                seen = set()
                j = 0
                while(j < 9):
                    element = None
                    if isVertical:
                        element = board[j][i]
                    else:
                        element = board[i][j]
                    
                    if element == ".":
                        j+=1
                        continue

                    if element in seen:
                        return False
                    else:
                        seen.add(element)
                    
                    j+=1
                i+=1
            return True
        
        def checkSubBoxes(board: List[List[str]]) -> bool:
            i = 0
            while i < 9:
                seen = set()
                j = 0
                while j < 9:
                    element = board[(i//3) * 3 + (j//3)][(i%3) * 3 + (j%3)]
                    if element == ".":
                        j+=1
                        continue

                    if element in seen:
                        return False
                    else:
                        seen.add(element)
                    j+=1
                i+=1
            return True
        
        def bitmaskMethod(board: List[List[str]]) -> bool:
            i = 0
            row, col, sub_box = [0] * 9, [0] * 9, [0] * 9
            while i < 9:
                j = 0
                while j < 9:
                    if board[i][j] == ".":
                        j+=1
                        continue
                    
                    val = int(board[i][j]) - 1
                    if row[i] & (1 << val):
                        return False
                    if col[j] & (1 << val):
                        return False
                    if sub_box[i+j] & (1 << val):
                        return False
                    
                    row |= val
                    col |= val
                    sub_box |= val
                    
                    j+=1
                i+=1

        return checkRowsCols(board, True) and checkRowsCols(board, False) and checkSubBoxes(board)




