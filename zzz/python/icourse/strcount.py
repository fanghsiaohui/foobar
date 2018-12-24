#!/usr/bin/env python3

def countchar(string):
    alphabet = {chr(ord('a') + i) : 0 for i in range(26)}
    for i in alphabet:
        alphabet[i] = string.lower().count(i)
    return [value for key, value in sorted(alphabet.items())]

if __name__ == "__main__":
    string = input()
    print(countchar(string))
