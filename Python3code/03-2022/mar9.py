# Add Binary Problem and Solution : https://leetcode.com/problems/add-binary/submissions/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        x = int(a, 2)
        y = int(b, 2)
        # just convert to binary

        z = x + y
        # add

        r = str(bin(z))
        r = r[2:]
        # return as string haha
        return r

if __name__ == "__main__":
    test_a = "11"
    test_b = "1"
    test_obj = Solution()

    print(test_obj.addBinary(test_a, test_b))
