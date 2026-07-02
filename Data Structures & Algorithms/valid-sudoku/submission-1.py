class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[0 for _ in range(10)] for _ in range(9)]
        rows = [[0 for _ in range(10)] for _ in range(9)]
        matrix = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                else:
                    num = int(num)
                if rows[i][num] != 0:
                    return False
                else:
                    rows[i][num] = 1
                if cols[j][num] != 0:
                    return False
                else:
                    cols[j][num] = 1
                if matrix[i // 3][j // 3][num] != 0:
                    return False
                else:
                    matrix[i // 3][j // 3][num] = 1
        return True