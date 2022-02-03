string = input().split(" ")  # read a string words from the user split with space and put them in a list
palindrome_word = input()  # read a palindrome word from the user
palindromes = [word for word in string if word == word[::-1]] # use a comprehension to find all the words which are
# palindromes

print(palindromes)
print(f"Found palindrome {string.count(palindrome_word)} times")
