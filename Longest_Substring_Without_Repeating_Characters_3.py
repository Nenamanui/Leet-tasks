# Time:   O(n**2)
# Space:  O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ''
        length = 0
        for symb in s:
            sub_str += symb
            if len(sub_str) == len(set(sub_str)):
                length = len(sub_str)
            else:
                sub_str = sub_str[1:]
        return length




# Time:   O(n)
# Space:  O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_char = {}
        max_len = 0
        left = 0
        for right, char in enumerate(s):
            if char in dict_char and left <= dict_char[char]:
                left = dict_char[char] + 1
            dict_char[char] = right
            diff = right - left + 1
            max_len = max(diff, max_len)
        return max_len
