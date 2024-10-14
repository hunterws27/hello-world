import string

def decrypt(text, distance):
    result = ''
    for char in text:
        if char in string.printable:
            new_index = (string.printable.index(char) - distance) % len(string.printable)
            result += string.printable[new_index]
        else:
            result += char
    return result
def main():
    ciphertext = input("Enter the encrypted text: ")
    distance = int(input("Enter the distance value: "))
    decrypted_text = decrypt(ciphertext, distance)
    print("Decrypted text:", decrypted_text)
if __name__ == "__main__":
    main()
