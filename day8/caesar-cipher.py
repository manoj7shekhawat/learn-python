#!/usr/bin/env python3

import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    nt = ""
    if shift >= 52:
        shift %= 26
    for x in text:
        if x in alphabet:
            idx = alphabet.index(x)
            if direction == "de":
                if idx - shift < 0:
                    idx = abs(len(alphabet) + idx - shift)
                else:
                    idx -= shift
            else:
                if idx + shift > len(alphabet) - 1:
                    idx = abs(len(alphabet) - idx - shift)
                else:
                    idx += shift
            nt += alphabet[idx]
        else:
            nt += x

    if direction == "de":
        print("Decrypted text: " + nt)
    else:
        print("Encrypted text: " + nt)

print(art.logo)

while True:
    direction = input("Type 'en' to encrypt, type 'decode' to de, type 'st' to stop: ")
    if direction == "en" or direction == "de":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
    else:
        print("Stopping")
        break

    caesar(text, shift, direction)
