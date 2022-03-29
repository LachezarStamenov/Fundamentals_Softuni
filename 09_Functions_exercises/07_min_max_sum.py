list_of_int = input().split()

print(f"The minimum number is {min(map(int,list_of_int))}")
print(f"The maximum number is {max(map(int, list_of_int))}")
print(f"The sum number is: {sum(map(int, list_of_int))}")

# def min_max_sum_func(numbers):
#     print(f"The minimum number is {min(numbers)}")
#     print(f"The maximum number is {max(numbers)}")
#     print(f"The sum number is: {sum(numbers)}")
#
# nums = list(map(int, input().split()))
# min_max_sum_func(nums)