class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        cols_sets = defaultdict(set)
        rows_sets = defaultdict(set)
        squares_sets = defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows_sets[row] or
                   board[row][col] in cols_sets[col] or
                   board[row][col] in squares_sets[(row//3, col//3)]):
                   return False
                cols_sets[col].add(board[row][col])
                rows_sets[row].add(board[row][col])
                squares_sets[(row//3,col//3)].add(board[row][col])
        return True



