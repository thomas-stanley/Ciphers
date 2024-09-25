import string
letters = string.ascii_lowercase
to_encode = input("What to encode? ")
key = input("Key ")
answer = ""
for i in range(len(to_encode)):
    encode_letter = to_encode[i]
    key_letter = key[i]
    answer_pos = (letters.find(encode_letter) + letters.find(key_letter)) % 26
    answer += letters[answer_pos]
print(answer)
