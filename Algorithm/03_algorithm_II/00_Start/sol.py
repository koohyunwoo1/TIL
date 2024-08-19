print(int(10))  # 10진수
print(10)
print(bin(10))  # 주의. 문자열임
print(type(bin(10)))
print(oct(10))  # 8진법
print(hex(18))  # 16진법

# 16진법 -> 10진법
print(int('F', base=16))

print(bin(8)[2:].zfill(4))
print(bin(1)[2:].zfill(4))
for i in range(8):
    print(bin(i)[2:].zfill(4))

for i in range(16):
    print(bin(int(hex(i)[2:], base=16))[2:].zfill(4))

bin_to_hex = {}
for i in range(16):
    '''
    { '0000': 1,
        ...
      '1111' : F
    '''
    # bin_to_hex[2진법 4비트]: 16
    # bin_to_hex[bin(i)[2:].zfill(4)]
    print(f'{i:04b}', 'f-string')
    bin_to_hex[f'{i:04b}'] = hex(i)[2:].upper()         # 대문자
    # bin_to_hex[f'{i:04b}'] = hex(i).replace('0x', '')   # 소문자

print(bin_to_hex)
hex_to_bin = {hex(i).replace('0x', '').upper(): f'{i:04b}' for i in range(16)}
print(hex_to_bin)