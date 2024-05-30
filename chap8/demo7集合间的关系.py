# Author: lisz1012
# Creation date and time: 5/29/24 7:57 PM

s = {10, 20, 30, 40}
s2 = {30, 40, 20, 10}
print(s == s2)  # True, 因为集合是无序的, 只要元素相同就相等

# 判断子集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))  # True
print(s3.issubset(s1))  # False, 因为90不在s1中

# 判断超集
print(s1.issuperset(s2))  # True
print(s1.issuperset(s3))  # False, 因为90不在s1中

# 判断两个集合是否没有交集
print(s2.isdisjoint(s3))     # False, 因为s2和s3有交集, 如果没有交集则返回True
s4 = {100, 200, 300}
print(s2.isdisjoint(s4))  # True, 因为s2和s3没有交集
