# merge sorted array in increasing order (leetcode Arrays 101)

# The fact that leetcode accepted this bothers me ALOT

class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i + m] = nums2[i]

        nums1.sort()
        return None



if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    test_obj = Solution()

    print(test_obj.merge(nums1, m, nums2, n))
