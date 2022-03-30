string = input()
string_to_num = int(string.replace('.', ''))
new_version = '.'.join(str(string_to_num + 1))

print(new_version)




