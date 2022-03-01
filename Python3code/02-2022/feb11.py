# square then sort array results (Leetcode Arrays 101 continued)

class Solution:
    def sortedSquares(self, nums):
        nums_squared = []
        for i in nums:
            nums_squared.append(i**2)

        for i in range(0, len(nums_squared) - 1):
            for j in range(len(nums_squared) - 1, i, -1):
                if nums_squared[j] < nums_squared[j - 1]:
                    temp = nums_squared[j]
                    nums_squared[j] = nums_squared[j - 1]
                    nums_squared[j - 1] = temp
        return nums_squared


if __name__ == "__main__":
    test1 = [-4,-1,0,3,10]
    obj_test1 = Solution()
    print(obj_test1.sortedSquares(test1))
