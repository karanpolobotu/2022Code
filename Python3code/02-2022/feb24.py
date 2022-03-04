# Sort Array by Parity (move odd numbers to end, even numbers to beginning)

class Solution:
    def paritySort(self, nums: list) -> list:
        # pointer for all
        i = 0
        # pointer for even
        j = i + 1

        while j < len(nums):
            if nums[i] % 2 != 0 and nums[j] % 2 != 0:
                # if both are odd, move j until it is even
                j += 1
            elif nums[i] % 2 != 0 and nums[j] % 2 == 0:
                # if j is even but i is odd, swap
                nums[i], nums[j] = nums[j], nums[i]
                # increase both by 1 to move forward
                i += 1
                j += 1
            else:
                i += 1
                j += 1

        return nums

if __name__ == "__main__":
    test_arr = [3,1,2,4]

    test_obj = Solution()
    print(test_obj.paritySort(test_arr))
