# Write a program that reads the path to a file and subtracts the file name and its extension.


# path = input()
#
# rightmost_index = lambda x, y: max([i for i in range(len(x)-1,-1,-1) if x[i]==y])
#
# ext_index = rightmost_index(path, '.')
#
# file_ext = path[ext_index + 1:]
#
# file_index = rightmost_index(path, '\\') + 1
#
# file_name_lenght = ext_index - file_index
#
# file_name = path[file_index:file_index + file_name_lenght]
#
# print(f'File name: {file_name}')
# print(f'File extension: {file_ext}')

file_path = input().split("\\")

last_file = file_path[-1].split('.')
name = last_file[0]
ext = last_file[1]
print(f'File name: {name}')
print(f'File extension: {ext}')
