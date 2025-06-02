# Encryption / Decryption Tool (Code in Place 2025)

*This application was created as the final project for Stanford's Code in Place 2025.*  
  
A simple terminal-based script to encrypt and decrypt messages, using the classic Caesar Cipher technique. 


## How it works

- This script uses the classic Caesar Cipher, which works by shifting each letter of the message by a fixed number of positions in the alphabet.
- Supports (and preserves) both uppercase and lowercase letters.
- Non-alphabetic characters are left unchanged.  

## Features

- Encrypt text with a user-defined shift value (including negative shifts)
- Decrypt text with a user-defined shift value (including negative shifts)
- Input validation for both options and shift values
- Easy-to-use interactive prompt  

## Usage

1. Clone the repo
2. Run the file:  `python caesar_encrypt_tool.py`
3. Follow the prompts  

## Example output

```text
Welcome to the Caesar Cipher Encryption tool!

Choose an option: "encrypt", "decrypt" or "quit": encrypt
Enter the shift number (can be negative): -7
Type the sentence you want to encrypt: I made this for Code in Place 2025!

Encrypting...

Your encrypted message is: B ftwx mabl yhk Vhwx bg Ietvx 2025!
```
  
## Requirements

- Python 3.x

