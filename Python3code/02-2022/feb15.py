# merge sorted array in increasing order (leetcode Arrays 101)

class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m] + nums2
        print(nums1)

        def merge_sort(arr):

            if len(arr) > 1:

                mid = len(arr)//2

                L = arr[:mid]
                R = arr[mid:]

                merge_sort(L)
                merge_sort(R)

                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
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

        merge_sort(nums1)

        print(nums1)
        return None



if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    test_obj = Solution()

    print(test_obj.merge(nums1, m, nums2, n))
