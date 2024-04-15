class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Returns true if x is palindrome, false

        >>> Solution().isPalindrome(121)
        True
        >>> Solution().isPalindrome(-121)
        False
        >>> Solution().isPalindrome(10)
        False
        """

        if x < 0:
            return False
        if x < 10:
            return True

        a = []
        while x != 0:
            a.append(x % 10)
            x //= 10

        for i in range(len(a)):
            if a[i] != a[-(1 + i)]:
                return False
        return True


if __name__ == '__main__':
    from doctest import testmod

    testmod()
