class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = len(s)

        seen = set()
        
        left = 0
        result = 0

        for right in range(l):
            curr = s[right]

            while curr in seen:
                seen.remove(s[left])
                left += 1

            seen.add(curr)
            result = max(result, right - left + 1)


        return result