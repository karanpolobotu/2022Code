# Arrays 101 = Leetcode

# Find numbers with even number of digits

class Solution:
    def findNumbers(self, nums) -> int:
        evenDigits = []
        for i in nums:
            holder = []
            valid = True
            j = 0
            while valid:
                a = i//10**j
                if a == 0:
                    j = 0
                    valid = False
                holder.append(a)
                j += 1

            if len(holder) % 2 == 1:
                evenDigits.append(i)

        return len(evenDigits)


if __name__ == "__main__":
    obj = Solution()
    obj1 = obj.findNumbers([555,901,482,1771])

    print(obj1)
