# move all Zeroes in a list to the back of the list while maintainig the order of the list (Arrays 101 leetcode)

# Two pointer leetcode system for deletion of duplicate elements

# O(n^2) time complexity solution, exceeded time limit but works

class Solution:
    def moveZeroes(self, arr: list) -> list:

        for j in range(len(arr) - 1):
            for i in range(len(arr) - 1):
                if arr[i] == 0:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp

        return arr

if __name__ == "__main__":
    test_arr = [0, 1, 0, 3, 12, 15, 0, 8, 4, 0]

    test_obj = Solution()
    print(test_obj.moveZeroes(test_arr))
