#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#this is my second project

import os, platform
import random, string


#clear terminal's screen
if platform.system().lower() == 'windows':
    os.system('cls')
else:
    os.system('clear')

def generate_password(lenWord, use_uppercase, use_digits, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(lenWord))
    return password

def main():
    print("=== Generator Kata Sandi ===")
    
    lenWord = int(input("Masukkan panjang kata sandi: "))
    use_uppercase = input("Gunakan huruf kapital? (ya/tidak): ").lower() == 'ya'
    use_digits = input("Gunakan angka? (ya/tidak): ").lower() == 'ya'
    use_symbols = input("Gunakan simbol? (ya/tidak): ").lower() == 'ya'

    kata_sandi = generate_password(lenWord, use_uppercase, use_digits, use_symbols)

    print("\nKata Sandi yang Dibuat:")
    print(kata_sandi)

if __name__ == "__main__":
    main()
