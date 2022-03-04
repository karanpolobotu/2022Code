class Solution:
    def heightChecker(self, heights: list) -> int:
        newArr = []
        for i in range(len(heights)):
            newArr.append(heights[i])

        mergesort(newArr)

        diff = 0
        for i in range(len(heights)):
            if heights[i] != newArr[i]:
                diff += 1

        return diff

def mergesort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1


        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

if __name__ == "__main__":
    test_arr = [3,1,2,4]

    test_obj = Solution()
    print(test_obj.heightChecker(test_arr))
