from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = Counter(nums).most_common(k)
        print(frequency)

        return []


nums = [1, 2, 2, 3, 3, 3, 4, 4, 4]
k = 2
solve = Solution()
print(solve.topKFrequent(nums, k))
