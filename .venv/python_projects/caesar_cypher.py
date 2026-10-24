import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase

def encrypt(message, shift):
    shifted_alphabet = lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]

    trans_table = str.maketrans(lower + upper, shifted_alphabet)
    encrypted_message = message.translate(trans_table)

    return encrypted_message

def decrypt(message, shift):
    shifted_alphabet = lower[-shift:] + lower[:-shift] + upper[-shift:] + upper[:-shift]

    trans_table = str.maketrans(lower + upper, shifted_alphabet)
    decrypted_message = message.translate(trans_table)

    return decrypted_message

slogan = 'And his name is John Cena!'
encrypted_slogan = encrypt(slogan, 3)
decrypted_slogan = decrypt(encrypted_slogan, 3)

print(encrypted_slogan)
print(decrypted_slogan)

