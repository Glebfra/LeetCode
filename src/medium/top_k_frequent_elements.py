from typing import List


class Solution:
    """
    >>> Solution().topKFrequent([1,1,1,2,2,3], 2)
    [1, 2]
    >>> Solution().topKFrequent([1], 1)
    [1]
    >>> Solution().topKFrequent([4,1,-1,2,-1,2,3], 2)
    [-1, 2]
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements = dict()
        for num in nums:
            if num not in frequent_elements:
                frequent_elements[num] = 0
            frequent_elements[num] += 1
        frequent_elements = sorted(frequent_elements.items(), key=lambda item: item[1], reverse=True)
        return list(map(lambda x: x[0], frequent_elements[:k]))


if __name__ == '__main__':
    from doctest import testmod

    testmod()
