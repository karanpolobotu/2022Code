#LEETCODE Problem 26, removing duplicates using in place algorithm. O(n)

#Need to find more efficient solution

#WILL ONLY RUN IN LEETCODE COMPILER, HERE: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #two pointer system, with first pointer defined
        i = 0

        for j in range(1, len(nums)):
            # second pointer defined
            if nums[j] != nums[i]:
                # if first pointer and second pointer point to different values
                i += 1
                # pointer i moves to next value
                nums[i] = nums[j]
                # value for pointer i equals pointer j

        return i + 1
