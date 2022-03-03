# check if list is a mountain array
# Leetcode, arrays 101

# so many exceptions....

class Solution:
    def validMountainArray(self, arr: list) -> bool:
        mountain = False
        peak = 0

        for i in range(1, len(arr) - 1):
            if arr[i] == arr[i - 1]:
                return False

            if arr[i] < arr[i - 1] and arr[i] <= arr[i + 1]:
                peak += 1
            if arr[i] > arr[i - 1] and arr[i] >= arr[i + 1]:
                peak += 1

            if peak >= 1 and arr[i] <= arr[i + 1]:
                return False

        if peak == 1:
            mountain = True

        return mountain

if __name__ == "__main__":
    test_arr = [1,1,1,1,1,1,1,2,1]

    test_obj = Solution()
    print(test_obj.validMountainArray(test_arr))
