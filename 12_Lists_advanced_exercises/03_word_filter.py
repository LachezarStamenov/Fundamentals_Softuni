words_as_text = input().split()
even_len_words = [word for word in words_as_text if len(word) % 2 == 0]
print(*even_len_words, sep='\n')