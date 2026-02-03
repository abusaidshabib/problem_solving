nums_list = [1, 2, 3,3, 4]


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # set can't save duplicate values.
        return len(nums) != len(set(nums))


solve = Solution()
print(solve.hasDuplicate(nums_list))

# using hash set (neetcode solution)
class Solution2:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


solve2 = Solution2()
print(solve2.hasDuplicate(nums_list))
