# Data Structures Practice - Leetcode (Arrays 101)

# Given an array, return the maximum number of ones that appear in sequence beside each other

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        sol = []
        count = 0
        for i in range(len(nums)):

            if nums[i] == 1:
                count += 1

            elif nums[i] == 0:
                sol.append(count)
                count = 0

        #incase there is no 0 at the end
        sol.append(count)
        return max(sol)


if __name__ == "__main__":
    obj = Solution()
    obj1 = obj.findMaxConsecutiveOnes([1,1,0,1,1,1])

    print(obj1)
