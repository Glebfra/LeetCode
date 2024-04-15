from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes the duplicates from list

        >>> Solution().removeDuplicates([1,1,2])
        2
        >>> Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        5
        """

        count = 0
        last_digit = -101
        for i in range(len(nums)):
            if nums[i] != last_digit:
                last_digit = nums[i]
                nums[count] = last_digit
                count += 1
        del nums[count:]
        return count


if __name__ == '__main__':
    from doctest import testmod

    testmod()
