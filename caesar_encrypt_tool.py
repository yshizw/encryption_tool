def main():
    initial_message()
    run_tool()


def initial_message():
    print("\nWelcome to the Caesar Cipher Encryption tool!\n")


def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                offset = 65
            else:
                offset = 97

            shifted = (ord(char) - offset + shift) % 26
            encrypted += chr(shifted + offset)
        else:
            encrypted += char

    return encrypted


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def shift_validation():
    while True:
        shift = input("Enter the shift number (can be negative): ").strip()
        if shift.lstrip("-").isdigit():
            return int(shift)
        print("Please input a valid number.")


def run_tool():
    user_choice = input("Choose an option: \"encrypt\", \"decrypt\" or \"quit\": ").strip().lower()
    while user_choice != "quit":
        if user_choice == "encrypt" or user_choice == "decrypt":
            shift_num = shift_validation()
            if user_choice == "encrypt":
                user_message = input("Type the sentence you want to encrypt: ")
                print("\nEncrypting...\n")
                print("Your encrypted message is: " + caesar_encrypt(user_message, shift_num))
            else:
                user_message = input("Type the sentence you want to decrypt: ")
                print("\nDecrypting...\n")
                print("Your decrypted message is: " + caesar_decrypt(user_message, shift_num))
        else:
            print("\nInvalid choice. Please type \"encrypt\", \"decrypt\" or \"quit\".")

        user_choice = input("\nChoose an option: \"encrypt\", \"decrypt\" or \"quit\": ").strip().lower()

    print("\nSee you again!")


if __name__ == "__main__":
    main()