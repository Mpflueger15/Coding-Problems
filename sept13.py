class Solution:
  def moveZeros(self, nums):
      for i in range(0, nums.count(0)):
          nums.append(nums.pop(nums.index(0)))
          print(i)



nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]