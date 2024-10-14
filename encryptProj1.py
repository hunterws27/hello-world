import string

def encrypt(text, distance):
    result = ''
    for char in text:
        if char in string.printable:
            new_index = (string.printable.index(char) + distance) % len(string.printable)
            result += string.printable[new_index]
        else:
            result += char
    return result
def main():
    plaintext = input("Enter the plaintext: ")
    distance = int(input("Enter the distance value: "))
    encrypted_text = encrypt(plaintext, distance)
    print("Encrypted text:", encrypted_text)
if __name__ == "__main__":
    main()
