def encrypt_caesar_cipher(text, shift):
    result = ""

    # Traverse the text
    for i in range(len(text)):
        char = text[i]

        
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Add non-alphabetic characters without encryption
        else:
            result += char

    return result

def decrypt_caesar_cipher(text, shift):
    return encrypt_caesar_cipher(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption Tool")
    while True:
        choice = input("\nWould you like to (E)ncrypt or (D)ecrypt a message? (Q to quit): ").upper()

        if choice == 'Q':
            break
        elif choice not in ['E', 'D']:
            print("Invalid option! Please choose 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")
            continue

        text = input("Enter your message: ")
        shift = int(input("Enter the shift value (e.g., 3): "))

        if choice == 'E':
            encrypted_text = encrypt_caesar_cipher(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        elif choice == 'D':
            decrypted_text = decrypt_caesar_cipher(text, shift)
            print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
