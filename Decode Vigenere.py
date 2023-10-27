letters = string.ascii_lowercase
keyword_len = int(input("Keyword length "))
characters = "".join(input("Characters ").split())
encoded_characters = "".join(input("Encoded characters ").split())
encoded_message = "".join(input("Encoded message ").split())
decoded_message = ""
key = ""
for num in range(len(characters)):
    for value in letters:
        position = (letters.find(value) + letters.find(characters[num])) % 26
        if position == letters.find(encoded_characters[num]):
            key += value
            break
    if len(key) == keyword_len:
        break
for i in range(len(encoded_message)):
    current_key = key[i % keyword_len]
    position = (26 + letters.find(encoded_message[i]) - letters.find(current_key)) % 26
    decoded_message += letters[position]
print(decoded_message.replace("x", " "))
