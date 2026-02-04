# work only when list is sorted

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) - 1

        while low < high:
            sum = nums[low] + nums[high]
            if sum == target:
                return [low, high]
            elif sum < target:
                low += 1
            else:
                high -= 1

        return []



nums = [-1,-2,-3,-4,-5]
target = -8

solve = Solution()
print(solve.twoSum(nums, target))


# unsorted list
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i,v in enumerate(nums):
            complement = target - v
            if complement in seen:
                return [seen[complement], i]
            seen[v] = i
        return []

solve2 = Solution2()
print(solve2.twoSum(nums, target))
