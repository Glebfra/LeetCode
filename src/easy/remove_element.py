from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        This function removes the element from list

        >>> Solution().removeElement([3,2,2,3], 3)
        2
        >>> Solution().removeElement([0,1,2,2,3,0,4,2], 2)
        5
        """

        index = 0
        nums_length = len(nums)
        while index < nums_length:
            if nums[index] == val:
                del nums[index]
                nums_length -= 1
            else:
                index += 1
        return nums_length


if __name__ == '__main__':
    from doctest import testmod

    testmod()
