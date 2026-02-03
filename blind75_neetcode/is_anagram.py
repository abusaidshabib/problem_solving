s = "jar"
t = "jam"


class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        s_dict = {}
        t_dict= {}
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
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

        for i in s_dict:
            if i in t_dict and t_dict[i] == s_dict[i]:
                continue
            else:
                return False

        return True


solve= Solution()
print(solve.isAnagram(s, t))

