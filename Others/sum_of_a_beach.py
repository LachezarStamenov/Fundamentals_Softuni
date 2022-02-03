string = input()
lower_case_string = string.lower()
first_word = lower_case_string.count('sand')
second_word = lower_case_string.count('water')
third_word = lower_case_string.count('fish')
forth_word = lower_case_string.count('sun')

total_counts = int(first_word) + int(second_word) + int(third_word) + int(forth_word)
print(total_counts)

