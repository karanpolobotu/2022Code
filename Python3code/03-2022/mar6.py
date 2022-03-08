# max Sub array problem and solution: Leetcode : https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list) -> int:

        # Kandane's algorithm

        maxSum = currentSum = nums[0]
        # keep track of current and max sum

        for i in range(1, len(nums)):
            # if current number adds to current sum and makes it larger, add it current sum
            currentSum = max(currentSum + nums[i], nums[i])
            # return the max sum between max sum and current sum. if current sum exceeds max sum, max sum becomes it
            maxSum = max(maxSum, currentSum)

        return maxSum


if __name__ == "__main__":

    test_arr = [-2,1,-3,4,-1,2,1,-5,4]

    test_obj = Solution()

    print(test_obj.maxSubArray(test_arr))
