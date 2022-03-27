key = int(input())
n = int(input())
massage = []
for num in range(n):
    letters = input()
    new_letter = ord(letters) + key
    massage.append(chr(new_letter))

print("".join(massage))