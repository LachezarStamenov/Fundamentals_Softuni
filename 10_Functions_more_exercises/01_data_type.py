def calculate_num_depending_of_type(type, num):
    """This is a function which make a calculations
    of the number based on the input type or print string"""
    global result
    if type == "int":
        result = int(num) * 2
    elif type == "real":
        result = "{:.2f}".format(float(num) * 1.5)
    elif type == "string":
        result = "$" + num + "$"
    return result


num_type = input()
num_as_str = input()

print(calculate_num_depending_of_type(num_type, num_as_str))