# 1.Concatination of array in Python
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums * 2

# 2.Shuffle the array in Python
class Solution(object):
    def shuffle(self, nums, n):
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        
        return result

# 3.Max Consecutive Ones in Python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 0
  
        return max_count
        