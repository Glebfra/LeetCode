class Solution:
    def minimumBoxes(self, n: int) -> int:
        """
        https://leetcode.com/problems/building-boxes/solutions/1032104/python3-math/

        >>> Solution().minimumBoxes(3)
        3
        >>> Solution().minimumBoxes(4)
        3
        >>> Solution().minimumBoxes(10)
        6
        >>> Solution().minimumBoxes(15)
        9
        """

        boxes_on_level = 0
        level = 0
        while n > 0:
            level += 1
            boxes_on_level += level
            n -= boxes_on_level

        return boxes_on_level


if __name__ == '__main__':
    from doctest import testmod

    testmod()
