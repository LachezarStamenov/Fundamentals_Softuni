nums = [int(el) for el in input().split(", ")] # четем числа като стринг и ги превръщаме в  list of int

group = 10 # групите ни започват от 10
max_number = max(nums) # намираме максималното число в листа

while nums: # докато има елементи в листа
    nums_group = []

    for num in nums:
        if num in range(group - 10, group + 1):
            nums_group.append(num)
    for num in nums_group:
        nums.remove(num)
    print(f"Group of {group}'s: {nums_group} ")
    group += 10