#!/usr/bin/env python3

from base64 import b16decode, b64encode


inputstring = input("Enter hex string to convert to base 64:")

data_hex = bytes(inputstring, 'utf-8')

hex_decoded = b16decode(data_hex,casefold=True)

base64_data = b64encode(hex_decoded)

print("Base64 of your string is: " + base64_data.decode())