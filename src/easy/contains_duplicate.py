from typing import List


class Solution:
    """
    >>> Solution().containsDuplicate([1,2,3,1])
    True
    >>> Solution().containsDuplicate([1,2,3,4])
    False
    >>> Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    True
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return not len(nums) == len(nums_set)


if __name__ == '__main__':
    from doctest import testmod

    testmod()
