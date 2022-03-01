#LEETCODE Problem 26, removing duplicates using in place algorithm. O(n^3), passes 360/361 test cases, case 361 is too large so the time is exceeded

#Need to find more efficient solution

#WILL ONLY RUN IN LEETCODE COMPILER, HERE: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = nums[-1]
        for i in range(len(nums) - 1):
            a = 0
            while nums[a] != k:
                if nums[a] == nums[a + 1]:
                    for j in range(a, len(nums) - 1):
                        temp = nums[j]
                        nums[j] = nums[j + 1]
                        nums[j + 1] = temp

                a += 1

        return nums.index(k) + 1
