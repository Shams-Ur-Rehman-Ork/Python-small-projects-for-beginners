user_input = input("Enter a phrase: ")
text_string = user_input.split()
acronym = ""

for item in text_string:
    acronym = acronym + item[0].upper()

print(acronym)


