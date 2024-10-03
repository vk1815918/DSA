from collections import Counter

list = ["a", "b", "c", "a", "b", "a", "a", "b"]

c = Counter(list)
print(c)
for k, v in c.items():
    print(k, " ", v)
    # print(c[i])
# print(c.items())