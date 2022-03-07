# March 4th leetcode problem and solution, Search Insert Position: https://leetcode.com/problems/search-insert-position/

import copy

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:

        #This solution works and runs in O(log n) time

        # iterative binary search, was so simple all along
        
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                return mid

        return low

if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7, 9, 10]
    test_val = 8

    test_obj = Solution()

    print(test_obj.searchInsert(test_nums, test_val))
