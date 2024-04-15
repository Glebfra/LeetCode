class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        The sum of 2 binary numbers

        >>> Solution().addBinary('11', '1')
        '100'
        >>> Solution().addBinary('1010', '1011')
        '10101'
        """

        c = (sum([int(a_i) * 2 ** i for i, a_i in enumerate(a[::-1])]) +
             sum([int(b_i) * 2 ** i for i, b_i in enumerate(b[::-1])]))
        return bin(c)[2:]


if __name__ == '__main__':
    from doctest import testmod

    testmod()
