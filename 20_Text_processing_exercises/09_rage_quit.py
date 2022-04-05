input_line = input().upper()
result = ''
unique_chars = set()
last_digit_index = current_digit_index = -1
for i in range(len(input_line)):
    if input_line[i].isdigit():
        current_digit_index = i
    if current_digit_index != last_digit_index:
        number_len = 1
        for j in range(i + 1, len(input_line), 1):
            if not input_line[j].isdigit():
                break
            number_len += 1
        num = int(input_line[i:number_len + i])
        text = input_line[last_digit_index + 1:i]
        if num > 0:
            for v in range(num):
                result += text
            for char in text:
                unique_chars.add(char)
        current_digit_index = current_digit_index + number_len - 1
        last_digit_index = current_digit_index
print(f"Unique symbols used: {len(unique_chars)}")
print(result)