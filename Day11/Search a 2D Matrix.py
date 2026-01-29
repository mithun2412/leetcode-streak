class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row * col - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // col][mid % col]

            if val == target:
                return True
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
