class Solution:
    def isValid(self, s: str) -> bool:
        """
        >>> Solution().isValid('()')
        True
        >>> Solution().isValid('()[]{}')
        True
        >>> Solution().isValid('(]')
        False
        >>> Solution().isValid('([])')
        True
        """
        pass
        

if __name__ == '__main__':
    from doctest import testmod

    testmod()
