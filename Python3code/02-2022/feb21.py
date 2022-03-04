# Two pointer leetcode system for deletion of duplicate elements

class Solution:
    def replaceElements(self, arr: list) -> list:
        #handle edge case
        while len(arr) > 0:
            #create pointer 1 that starts at second elem (1st elem is fine in place)
            writePointer = 1

            #go through each elem in array
            for readPointer in range(1, len(arr)):
                #if current elem is different from previous elem
                if (arr[readPointer] != arr[readPointer - 1]):
                    # copy it into the next position at the front, tracked by writePointer
                    arr[writePointer] = arr[readPointer]
                    #increment writePointer because next element should be written one space ver
                    writePointer += 1

        return arr

if __name__ == "__main__":
    test_arr = [1, 1, 2, 2, 3, 4, 5, 5]

    test_obj = Solution()
    print(test_obj.replaceElements(test_arr))
