# find dissappeared numbers - Arrays 101 (Leetcode)

class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        arr = []

        # go through list
        for i in range(len(nums)):
            # Index is the absolute value of index minus 1
            index = abs(nums[i]) - 1
            # if index is greater than 0
            if nums[index] > 0:
                # multiply by negative 1
                nums[index] *= (-1)

        for i in range(len(nums)):
            if nums[i] > 0:
                arr.append(i+1)
        return arr


if __name__ == "__main__":
    test_arr = [4,3,2,7,8,2,3,1]

    test_obj = Solution()
    print(test_obj.findDisappearedNumbers(test_arr))
