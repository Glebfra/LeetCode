from typing import List


class Solution:
    """
    >>> Solution().groupAnagrams([""])
    [['']]
    >>> Solution().groupAnagrams(["a"])
    [['a']]
    >>> Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = []
            anagram_dict[sorted_word].append(word)

        grouped_anagrams = []
        for anagram in anagram_dict.values():
            grouped_anagrams.append(anagram)
        return grouped_anagrams


if __name__ == '__main__':
    from doctest import testmod

    testmod()
