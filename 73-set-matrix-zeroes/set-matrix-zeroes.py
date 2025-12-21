class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        first_row = False
        for i in range(rows):
            for k in range(columns):
                if matrix[i][k] == 0:
                    matrix[0][k] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        first_row = True
        for i in range(1,rows):
            for k in range (1, columns):
                if matrix[i][0] == 0 or matrix[0][k] == 0:
                    matrix[i][k] = 0
        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0
        if first_row:
            for k in range(columns):
                matrix[0][k] = 0

