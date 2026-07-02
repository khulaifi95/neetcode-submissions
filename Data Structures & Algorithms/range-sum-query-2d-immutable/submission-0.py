class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        nrows = len(matrix)
        ncols = len(matrix[0])
        # row sum
        self.rec_sum = [[0] * (ncols + 1) for _ in range(nrows + 1)]
        
        for r in range(nrows):
            prefix = 0
            for c in range(ncols):
                prefix += matrix[r][c]
                above = self.rec_sum[r][c + 1]
                self.rec_sum[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        return self.rec_sum[r2][c2] - self.rec_sum[r1-1][c2] - self.rec_sum[r2][c1-1] + self.rec_sum[r1-1][c1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)