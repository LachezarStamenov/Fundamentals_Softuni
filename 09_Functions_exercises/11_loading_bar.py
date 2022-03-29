# def load_bar(n):
#     bar = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
#
#     if n == 0:
#         return bar
#
#     n = n // 10
#     for index in range(n):
#         bar[index] = "%"
#     return bar
#
#
# number = int(input())
# bar_result = load_bar(number)
#
# if bar_result.count("%") == 10:
#     print("100% Complete!")
#     print(f"[{''.join(bar_result)}]")
# else:
#     print(f"{number}% [{''.join(bar_result)}]")
#     print("Still loading...")


def loading_bar(num):

    if num == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        percent = (num//10) * '%'
        dots = (10 - (num // 10)) * '.'
        print(f'{num}% [{percent}{dots}]')
        print('Still loading...')

n = int(input())
loading_bar(n)