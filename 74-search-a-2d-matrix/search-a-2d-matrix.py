class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        column = len(matrix[0])
        i = 0
        j = row-1
        while(i<j):
            middle_row = i + (j-i)//2
            if matrix[middle_row][0] > target:
                j = middle_row-1
            elif matrix[middle_row][column-1] < target:
                i = middle_row+1
            else:
                break
        final_middle_row = i + (j-i)//2      
        a = 0
        b = column-1
        while (a<=b):
            middle = a + (b-a)//2 
            if matrix[final_middle_row][middle] > target:
                b = middle-1
            elif matrix[final_middle_row][middle] < target:
                a = middle+1
            elif matrix[final_middle_row][middle] == target:
                return True
        return False
        
