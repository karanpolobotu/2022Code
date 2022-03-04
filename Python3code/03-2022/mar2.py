# leetcode Recursion lesson

class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) - 1, -1, -1):
            s.append(s[i])

        s = s[len(s)//2:]
        print(s)

if __name__ == "__main__":

    s = ["H","a","n","n","a","h"]
    test_obj = Solution()
    print(test_obj.reverseString(s))
