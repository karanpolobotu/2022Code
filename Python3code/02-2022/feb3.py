# Day 1 of Leetcode practice

# Longest Common Prefix

def longestCommonStr(strs):
    #step 1: find lowest common element to use as prefix comparator

    def getMin():
        i = 0
        minL = strs[i]
        for i in range(len(strs) - 1):
            if strs[i] == "":
                minL = ""
                return minL
            if len(minL) > len(strs[i + 1]):
                minL = strs[i + 1]
        return minL
    #works, gives us minimum length
    prefix = ""
    newMin = getMin()
    print("minimum", newMin)
    num = len(newMin)
    for j in range(num):
        for i in strs:
            if newMin[j] != i[j]:
                return prefix
        prefix += newMin[j]

    return prefix

if __name__ == "__main__":
    strs = ["c", "acc", "ccc"]
    strs1 = ["ab", "a"]
    strs2 = ["flower", "flow", "flight"]
    strs3 = ["","cbc","c","ca"]
    strs4 = ["a","a","aabc","aa","acc"]
    print(longestCommonStr(strs))
    print(longestCommonStr(strs1))
    print(longestCommonStr(strs2))
    print(longestCommonStr(strs3))
    print(longestCommonStr(strs4))
