nums = int(input())
sum_of_char = 0
for num in range(nums):
    letters = input()
    sum_of_char += ord(letters)
print(f"The sum equals: {sum_of_char}")
