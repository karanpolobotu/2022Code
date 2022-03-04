# finds dissapeared numbers - Arrays 101

class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:

        arr = []
        for i in range(1, len(nums) + 1):
            arr.append(i)

        print(arr)

        diff = []
        for i in range(len(arr)):
            if arr[i] not in nums:
                diff.append(arr[i])

        return diff

if __name__ == "__main__":
    test_arr = [4,3,2,7,8,2,3,1]

    test_obj = Solution()
    print(test_obj.findDisappearedNumbers(test_arr))
