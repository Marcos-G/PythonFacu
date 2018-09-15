import struct

binary_file =open("data", "rb")
    # Read the whole file at once
data = binary_file.read()
print(data)
print(struct.unpack('i', data))
'''data=bytearray(data)
for i in range(len(data)):
    data[i]=data[i]^137
binary_file =open("secreto.pdf", "wb")
num_bytes_written = binary_file.write(data)
'''
