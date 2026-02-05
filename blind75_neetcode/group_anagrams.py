strs = ["act", "pots", "tops", "cat", "stop", "hat"]

from collections import Counter

# solution 1 by sorting
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        temp_dict = {}
        op_dict = {}
        result = []

        for i in strs:
            op_dict[i] = ''.join(sorted(i))

        for i in op_dict:
            if op_dict[i] in temp_dict:
                temp_dict[op_dict[i]].append(i)
            else:
                temp_dict[op_dict[i]] = [i]

        for i in temp_dict:
            result.append(temp_dict[i])

        return result


# solve = Solution()
# print(solve.groupAnagrams(strs))

# without sorting


strs = ["act", "pots", "tops", "cat", "stop", "hat"]


class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        op_dict = {}
        result = []

        for word in strs:
            key = ''.join(sorted(word))
            if key in op_dict:
                op_dict[key].append(word)
            else:
                op_dict[key] = []
                op_dict[key].append(word)

        return list(op_dict.values())


solve = Solution2()
print(solve.groupAnagrams(strs))

from collections import Counter, defaultdict

# using hashmap


class Solution3:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(word)

        print(dict(res))

        return list(res.values())

# data
"""
{
(1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['act', 'cat'],
(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0): ['pots', 'tops', 'stop'],
(1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['hat']
}
"""

solve3 = Solution3()
print(solve3.groupAnagrams(strs))

