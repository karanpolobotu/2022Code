class Solution:
    def replaceElements(self, arr: list) -> list:
        if not arr:
            return []
        newArr = [-1]
        hldr = [arr[-1]]
        for i in range(len(arr)-2, -1, -1):
            newArr.append(hldr[-1])
            if arr[i] > hldr[-1]:
                hldr[-1] = arr[i]
        return (newArr[::-1])

if __name__ == "__main__":
    test_arr = [17,18,5,4,6,1]

    test_obj = Solution()
    print(test_obj.replaceElements(test_arr))
