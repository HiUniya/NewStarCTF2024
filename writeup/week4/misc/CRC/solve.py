import zlib
import struct

filename = 'flag.png'
with open(filename, 'rb') as f:
    all_b = f.read()
    crc32key = int(all_b[29:33].hex(), 16)
    data = bytearray(all_b[12:29])
    n = 4095  # 理论上0xffffffff,但考虑到屏幕实际/cpu，0x0fff就差不多了
    for w in range(n):  # 高和宽一起爆破
        width = bytearray(struct.pack('>i', w))  # q为8字节，i为4字节，h为2字节
        for h in range(n):
            height = bytearray(struct.pack('>i', h))
            for x in range(4):
                data[x + 4] = width[x]
                data[x + 8] = height[x]
            crc32result = zlib.crc32(data)
            if crc32result == crc32key:
                # 2021.7.20，有时候显示的宽高依然看不出具体的值，干脆输出data部分
                print(data.hex())
                print("宽为：", end="")
                print(width)
                print("高为：", end="")
                print(height)
                exit(0)
"""
\x00\x00\x01\xf4

000001f4
4+15*16+16*16
49484452000001f4000001f40806000000
宽为：bytearray(b'\x00\x00\x01\xf4')
高为：bytearray(b'\x00\x00\x01\xf4')