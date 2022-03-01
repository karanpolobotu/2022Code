# duplicate zeroes in input

class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        newArr = []
        for i in arr:
            if i == 0:
                newArr.append(i)
                newArr.append(i)
            else:
                newArr.append(i)

        arr = newArr
        return arr

if __name__ == "__main__":
    test_arr = [1,0,2,3,0,4,5,0]
    test_obj = Solution()
    print(test_obj.duplicateZeros(test_arr))
