from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        """
        >>> Solution().maximumValue(["alic3","bob","3","4","00000"])
        5
        >>> Solution().maximumValue(["1","01","001","0001"])
        1
        """
        maxValue = 0
        for s in strs:
            try:
                temp = int(s)
            except:
                temp = len(s)
            if temp > maxValue:
                maxValue = temp
        return maxValue


if __name__ == '__main__':
    from doctest import testmod

    testmod()
