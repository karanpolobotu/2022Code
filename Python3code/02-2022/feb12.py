# square then sort array results (Leetcode Arrays 101 continued)

class Solution:
    def sortedSquares(self, nums):
        numsSQ = []
        for i in nums:
            numsSQ.append(i**2)

        # O(n log n) algorithm implemented for numsSQ

        return mergesort(numsSQ)

def mergesort(arr):
    if len(arr) > 1:
        # split midpoint
        mid = len(arr)//2

        # create left sub-array
        L = arr[mid:]
        # create right sub-array
        R = arr[:mid]

        #call mergesort of subarrays
        mergesort(L)
        mergesort(R)

        #insert into array
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
    test1 = [-4,-1,0,3,10]
    obj_test1 = Solution()
    print(obj_test1.sortedSquares(test1))
