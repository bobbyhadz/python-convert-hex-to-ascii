# How to convert from HEX to ASCII in Python

hex_str = '626f6262796861647a2e636f6d'

result = bytearray.fromhex(
    hex_str
).decode()

print(result) # 👉️ bobbyhadz.com