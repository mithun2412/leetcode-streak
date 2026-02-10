class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        if not matrix: 
            return result

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # left → right (top row)
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # top → bottom (right column)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # right → left (bottom row)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # bottom → top (left column)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
