# substrings = input().split(', ')
# words = input().split(',')
#
# occ_substring = []
#
# for substr in substrings:
#     for word in words:
#         if substr in word:
#             occ_substring.append(substr)
#
# print(sorted(set(occ_substring), key=occ_substring.index))


# with comprehension

substrings = input().split(', ')
words = input().split(',')

occ_substring = [substr for substr in substrings for word in words  if substr in word]

print(sorted(set(occ_substring), key=occ_substring.index))