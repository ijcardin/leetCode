class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = {}
        temp = []

        for num in nums:
            uniqueNums[num] = uniqueNums.get(num, 0) + 1

        for key in uniqueNums.keys():
            temp.append(key)

        temp.sort()
        newLen = len(temp)

        for i in range(len(temp)):
            nums[i] = temp[i]
        return newLen
        
        