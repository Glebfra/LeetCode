from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        This function generates the pascal triangle

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


if __name__ == '__main__':
    from doctest import testmod

    testmod()
