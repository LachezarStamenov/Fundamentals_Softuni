number = input()
text = ""
if number == "88":
    text = "Leo finally won the Oscar! Leo is happy"
elif number == "86":
    text = "Not even for Wolf of Wall Street?!"
elif not number == "88" and not number == "86" and number < "88":
    text = "When will you give Leo an Oscar?"
elif number > "88":
    text = "Leo got one already!"
print(text)