number = int(input())
bytes_values = number.to_bytes(2, byteorder='little')
byte_value = 0
for value in bytes_values:
    byte_value += value
print(byte_value)