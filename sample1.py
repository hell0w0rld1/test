print("hello world")

test_set = {"abc", "def"}
test_set.add("ghi")

print(test_set)  # {'def, 'abc', 'ghi'} ※出力順は実行の都度異なる


a = [i for i in range(10)]
print(a)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# a[start:end:step]
print(a[3:7])  # [3, 4, 5, 6]
print(a[::2])  # [0, 2, 4, 6, 8]