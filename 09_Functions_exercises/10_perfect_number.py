def is_num_perfect(num):
    proper_devisor = []

    for current_num in range(1, num):
        if num % current_num == 0:
            proper_devisor.append(current_num)

    if sum(proper_devisor) == num:
        return True
    return False

n = int(input())

if is_num_perfect(n):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
