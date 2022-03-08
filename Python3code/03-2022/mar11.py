# Climbing Stairs Problem (leetcode) - https://leetcode.com/problems/climbing-stairs/submissions/

class Solution:
    def climbStairs(self, n: int) -> int:

        # edge case
        if n == 1:
            return n
        if n == 2:
            return 2
        # Fibonacci Sequence...

        n1, n2 = 0, 1

        count = 0

        while count < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

        return nth

if __name__ == "__main__":
    test_code = 5
    test_obj = Solution()
    print(test_obj.climbStairs(test_code))
    
