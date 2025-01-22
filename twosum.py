# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
class TwoSum:
    def __init__(self, list1, target):
        self.list1 = list1
        self.target = target

    def solution(self):
        length = len(list1)

        for i in range(length-1):
            for j in range(i+1, length):
                if list1[i]+list1[j] == self.target:
                    new_list = i, j
                    return list(new_list)
        return -1


list1 = [1, 2, 4, 5, 11]
target = 6
obj = TwoSum(list1, target)
print(obj.solution())
