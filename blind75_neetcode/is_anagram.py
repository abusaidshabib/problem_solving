from collections import Counter

s = "jam"
t = "jam"


class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        s_dict = {}
        t_dict= {}
        if len(s) != len(t):
            return False
        for i in range(0, len(s)): # o(n)
            value_s = s[i]
            value_t = t[i]
            if value_s in s_dict:
                s_dict[value_s] = s_dict[value_s] + 1
            else:
                s_dict[value_s] = 1

            if value_t in t_dict:
                t_dict[value_t] = t_dict[value_t] + 1
            else:
                t_dict[value_t] = 1

        if s_dict != t_dict:
            return False

        return True


solve= Solution()
print(solve.isAnagram(s, t))


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = Counter(s) # O(n)
        t_dict = Counter(t) # O(m)
        if s_dict != t_dict:
            return False
        return True


solve2 = Solution2()
print(solve2.isAnagram(s, t))


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

        return all(v == 0 for v in count.values())

solve3 = Solution3()
print(solve3.isAnagram(s,t))
