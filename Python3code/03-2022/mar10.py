# leetcode Sqrt(x) problem and solution: https://leetcode.com/problems/sqrtx/submissions/

# return square root rounded down

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        for i in range(x):
            if (i * i) <= x and ((i + 1) * (i + 1)) > x:
                return i

if __name__ == "__main__":
    test = 8

    test_obj = Solution()
    print(test_obj.mySqrt(test))
