from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Returns the longest common prefix

        >>> Solution().longestCommonPrefix(['flower', 'flow', 'flight'])
        'fl'
        >>> Solution().longestCommonPrefix(['dog', 'racecar', 'car'])
        ''
        >>> Solution().longestCommonPrefix([''])
        ''
        >>> Solution().longestCommonPrefix([])
        ''
        >>> Solution().longestCommonPrefix(['a'])
        'a'
        """

        if len(strs) == 0:
            return ''

        symbols = []
        min_i = min([len(word) for word in strs])
        for i in range(min_i):
            symbol = (strs[0][i])
            for word in strs:
                if word[i] != symbol:
                    return ''.join(symbols)
            symbols.append(symbol)
        return ''.join(symbols)


if __name__ == '__main__':
    from doctest import testmod

    testmod()
