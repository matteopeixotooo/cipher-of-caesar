alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, direction_message):
    code_text = ""
    if direction_message == 'encode':
        for char in original_text:
            if char in alphabet:
                move_original_text = (alphabet.index(char) + shift_amount) % 26
                code_text += alphabet[move_original_text]
            elif char == ' ':
                code_text += " "
            else:
                code_text += char
        print(code_text)
    elif direction_message == 'decode':
        for char in original_text:
            if char in alphabet:
                move_original_text = (alphabet.index(char) - shift_amount) % 26
                code_text += alphabet[move_original_text]
            elif char == ' ':
                code_text += " "
            else:
                code_text += char
        print(code_text)

final = ""
while final != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        final = input("Type 'yes' to continue or 'no' to break: \n").lower()
    else:
        direction = input("Invalide Value! Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
        final = input("Type 'yes' to continue or 'no' to break: \n").lower()
