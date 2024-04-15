from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        This method generates the pascal triangle

        >>> Solution().generate(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        >>> Solution().generate(1)
        [[1]]
        """

        triangle = [[1]]
        for i in range(1, numRows):
            triangle.append([1]*(i+1))
            for j in range(i-1):
                triangle[i][j+1] = triangle[i-1][j] + triangle[i-1][j+1]
        return triangle

    def getRow(self, rowIndex: int) -> List[int]:
        """
        This method return the pascal triangle row

        >>> Solution().getRow(3)
        [1, 3, 3, 1]
        >>> Solution().getRow(0)
        [1]
        >>> Solution().getRow(1)
        [1, 1]
        """

        triangle = [1]
        for i in range(rowIndex):
            prev_triangle = triangle.copy()
            triangle.append(1)
            for j in range(1, i+1):
                triangle[j] = prev_triangle[j-1] + prev_triangle[j]
        return triangle


if __name__ == '__main__':
    from doctest import testmod

    testmod()
