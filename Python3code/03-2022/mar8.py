# add one to the array and return it as an array (problem and solution): https://leetcode.com/problems/plus-one/

import math
class Solution:
    def plusOne(self, digits: list) -> list:

        # convert to number first
        n = len(digits) - 1
        num = 0
        for i in range(len(digits)):
            num += (digits[i] * (10**n))
            n -= 1

        num = num + 1

        # convert back to array
        n = math.floor(math.log10(num))
        n = int(n)

        newDigits = []
        while n > -1:
            newDigits.append(num // (10 ** n))
            num = num % (10 ** n)
            n -= 1

        return newDigits


if __name__ == "__main__":
    test_arr = [9, 9]

    test_obj = Solution()

    print(test_obj.plusOne(test_arr))
