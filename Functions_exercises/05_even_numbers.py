list_of_integers = map(int, (input().split()))
result = filter(lambda x: x % 2 == 0, list_of_integers)
print(list(result))
