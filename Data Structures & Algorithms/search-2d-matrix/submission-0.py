class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bottom = len(matrix)-1

        while top <= bottom:
            mid = (top + bottom) // 2
            if (target == matrix[mid][0] 
            or target == matrix[mid][len(matrix[mid])-1]):
                return True
            elif target > matrix[mid][len(matrix[mid])-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else: #we are in the right row
                top = 1
                bottom = 0

                left = 0
                right = len(matrix[mid]) - 1
                while left <= right :
                    inner_mid = (left + right) // 2
                    if target == matrix[mid][inner_mid]:
                        return True
                    elif target < matrix[mid][inner_mid]:
                        right = inner_mid - 1
                    else:
                        left = inner_mid + 1
        return False