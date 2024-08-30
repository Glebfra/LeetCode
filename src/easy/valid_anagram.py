class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        >>> Solution().isAnagram('anagram', 'nagaram')
        True
        >>> Solution().isAnagram('rat', 'car')
        False
        """
        
        first_word = dict()
        for char in s:
            if char not in first_word.keys():
                first_word[char] = 0
            first_word[char] += 1
        
        for char in t:
            if char not in first_word.keys():
                return False
            first_word[char] -= 1
        
        for word in first_word.values():
            if word != 0:
                return False
        
        return True



if __name__ == '__main__':
    from doctest import testmod

    testmod()
