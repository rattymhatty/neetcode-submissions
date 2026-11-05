class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_length = 0, 0
        d = dict()
        for end in range(len(s)):
            if d.get(s[end]) is None or start > d[s[end]]:
                d[s[end]] = end
                max_length = max(max_length, end - start + 1)
            else:
                start = d[s[end]] + 1
                d[s[end]] = end
        return max_length
