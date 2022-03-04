# return third maximum largest number - leetcode Arrays 101

class Solution:
    def thirdMax(self, nums: list) -> int:
        nums.sort()
        z = set(nums)

        if len(z) < 3:
            return max(z)

        a = max(z)
        z.remove(a)
        b = max(z)
        z.remove(b)
        c = max(z)
        return c
        
if __name__ == "__main__":
    test_arr = [3,1,2,4]

    test_obj = Solution()
    print(test_obj.thirdMax(test_arr))
