# length of last word problem and solution on leetcode: https://leetcode.com/problems/length-of-last-word/submissions/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # handles the case where the last word is followed by several spaces
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                s = s[:i]
            elif s[i] != " ":
                break

        wordCount = 0
        # go in reverse, count instance of letters. If space, break and return letter count
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                wordCount += 1
            if s[i] == " ":
                break

        return wordCount

if __name__ == "__main__":
    test_s = "Hello World  "

    test_obj = Solution()
    print(test_obj.lengthOfLastWord(test_s))
