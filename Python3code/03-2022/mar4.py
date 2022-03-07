# March 4th leetcode problem and solution, Search Insert Position: https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:

        #This solution works but will not be accepted due to runtime being O(n)

        pos = 0

        #edge cases
        if target > nums[-1]:
            return len(nums)

        if target < nums[0]:
            return 0

        for i in range(1, len(nums) - 1):
            if (target > nums[i - 1]) and (target < nums[i + 1]):
                return pos + 1

            else:
                pos += 1

        # DNE condition
        return -1

if __name__ == "__main__":
    test_arr = [1, 3, 5, 6]
    test_val = 0

    test_obj = Solution()

    print(test_obj.searchInsert(test_arr, test_val))
