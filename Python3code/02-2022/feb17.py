# Arrays 101 remove element
# This problem is poorly worded. Not to mention the test cases are wrong and specifically caused me to make a longwinded approach to this problem
class Solution:
    def removeElement(self, nums, val):
        j = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[j] = nums[i]
                j += 1
        return j



if __name__ == "__main__":


    nums = [0,1,2,2,3,0,4,2]
    val = 2

    test_obj = Solution()
    print(test_obj.removeElement(nums, val))
