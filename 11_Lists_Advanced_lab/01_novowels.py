def no_vowel_sort(the_list):
    vowels = ["a", "e", "i", "o", "u"]
    return [''.join([c for c in word if c.lower() not in vowels]) for word in the_list]


lst = input().split()
print(*no_vowel_sort(lst), sep="")
