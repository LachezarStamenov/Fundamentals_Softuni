def additional_func(partition):
    current_max_num = 0
    special_char = ''

    for ch in partition:
        if ch != special_char:
            if current_max_num >= 6:
                break
            current_max_num = 1
            special_char = ch
        else:
            current_max_num += 1
    return [current_max_num, special_char]


def ticket_validator(ticket):
    ticket_condition = ''

    if len(ticket) != 20:
        ticket_condition = "invalid ticket"
    elif ticket[0] * 20 == ticket and ticket[0] in '@#$^':
        ticket_condition = f'ticket "{ticket}" - 10{ticket[0]} Jackpot!'
    else:
        data_source = ''
        if additional_func(ticket[0:10]) > additional_func(ticket[10:]):
            data_source = additional_func(ticket[10:])
        else:
            data_source = additional_func(ticket[0:10])

        number_of_special_signs = data_source[0]
        special_sign = data_source[1]

        if number_of_special_signs < 6 or special_sign not in '@#$^':
            ticket_condition = f'ticket "{ticket}" - no match'
        else:
            ticket_condition = f'ticket "{ticket}" - {number_of_special_signs}{special_sign}'

    return ticket_condition


def winning_ticket(data):
    for ticket in data:
        print(ticket_validator(ticket))


tickets_info = input()
data = [x.strip() for x in tickets_info.split(',')]
winning_ticket(data)







# def if_win(ticket):
#     left_half = ticket[0:10]
#     right_half = ticket[10:20]
#     combination = ''
#     win = False
#     symbol = None
#     for s in winning_symbols:
#         combination = ''
#         for i in range(6):
#             combination += s
#         if combination in left_half and combination in right_half:
#             win = True
#             symbol = s
#             break
#     return [win, symbol]
#
#
# def count_s(ticket, s):
#     left_half = list(ticket[0:10])
#     right_half = list(ticket[10:20])
#     lc = left_half.count(s)
#     rc = right_half.count(s)
#
#     return min([lc, rc])
#
#
# tickets = input().split(',')
# winning_symbols = ['@', '#', '$', '^']
# for ticket in tickets:
#     ticket = ticket.split()[0]
#     if len(ticket) != 20:
#         print("invalid ticket")
#         continue
#     if if_win(ticket)[0]:
#         if count_s(ticket, if_win(ticket)[1]) == 10:
#             print(f'ticket "{ticket}" - {10}{if_win(ticket)[1]} Jackpot!')
#         else:
#             print(f'ticket "{ticket}" - {count_s(ticket, if_win(ticket)[1])}{if_win(ticket)[1]}')
#     else:
#         print(f'ticket "{ticket}" - no match')