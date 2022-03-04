# Arrays 101 leetcode - moveZeroes

class Solution:
    def moveZeroes(self, nums: list) -> list:
        #two pointer solution
        i = 0
        j = i + 1

        while j < len(nums):
            if nums[i] == 0 and nums[j] == 0:
                # if both are equal to 0, move j to non zero pointer
                j += 1
            elif nums[i] == 0 and nums[j] != 0:
                # if i points to 0 and j points to non 0, swap
                nums[i], nums[j] = nums[j], nums[i]
                # increase both by 1 to move forward
                i += 1
                j += 1
            else:
                # if i points to non 0 or 0 and j points to 0, move both forward
                i += 1
                j += 1

        return nums

if __name__ == "__main__":
    test_arr = [0, 1, 0, 3, 12, 15, 0, 8, 4, 0]

    test_obj = Solution()
    print(test_obj.moveZeroes(test_arr))
