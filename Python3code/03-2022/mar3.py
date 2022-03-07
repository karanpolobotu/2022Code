# Leetcode problem and solution to Implement strStr(): https://leetcode.com/problems/implement-strstr/submissions/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        count, a, b = 0, len(needle), len(haystack)

        for i in range(0, b - a + 1):

            if haystack[i:i+a] == needle:
                return i


        return -1

if __name__ == "__main__":
    test_needle = ""
    test_haystack = ""

    test_obj = Solution()

    print(test_obj.strStr(test_haystack, test_needle))
