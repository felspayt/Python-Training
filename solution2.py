user_string = input("Please enter a string  ")
even_characters = []
for i in range(len(user_string)):
    if i % 2 == 0:
        even_characters.append(user_string[i])
    else:
        even_characters.append(user_string[i])
print(even_characters)
###################################
user_string = input("Please enter a string  ")
for i in range(len(user_string)):
    if i % 2 == 0:
        print(user_string[i])
###################################
user_string = input("Please enter a string  ")
for i in user_string:
    print(user_string[::2])