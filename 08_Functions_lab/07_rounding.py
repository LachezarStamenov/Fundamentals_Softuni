def rounding_the_string(string):
    rounded_list = [round(float(num)) for num in string]
    return rounded_list


lst = input().split()
print(rounding_the_string(lst))