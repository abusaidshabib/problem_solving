from collections import Counter, defaultdict

str_list = ['a','b','a','a','b']
num_list = [1,2,3,4,5,6,7]

print(Counter(str_list))

d = defaultdict(int)
for ch in str_list:
    d[ch] += 1

print(d)