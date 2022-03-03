# check if the list has two elements such that one is either half or twice of another
# Arrays 101 - leetcode
# first shot, not bad haha. 

class Solution:
    def checkIfExist(self, arr: list) -> bool:
        exist = False
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] == arr[j] / 2) or (arr[i] == arr[j] * 2):
                    print(arr[i], arr[j])
                    exist = True
                    break

        return exist
if __name__ == "__main__":
    test_arr = [3, 1, 7, 11]
    test_obj = Solution()
    print(test_obj.checkIfExist(test_arr))
