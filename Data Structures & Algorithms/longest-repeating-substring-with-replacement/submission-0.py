class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = dict()
        start, max_freq, max_length = 0, 0, 0
        for end in range(len(s)):
            d[s[end]] = d.get(s[end], 0) + 1
            max_freq = max(max_freq, d[s[end]])
            if end - start + 1 - max_freq <= k:
                max_length = max(max_length, end-start+1)
            else:
                while end - start + 1 - max_freq > k:
                    d[s[start]] -= 1
                    start += 1
        return max_length