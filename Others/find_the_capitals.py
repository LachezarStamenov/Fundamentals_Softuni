# Python3 code to demonstrate working of
# Uppercase Indices
# Using enumerate() + isupper()

# initializing string
test_str = input()

# Uppercase check using isupper()
# enumerate() gets indices
# res = [idx for idx, chr in enumerate(test_str) if chr.isupper()]
res = [idx for idx in range(len(test_str)) if test_str[idx].isupper()]
# printing result
print(str(res))
