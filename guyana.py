binary_file =open("secreto.pdf", "rb")
    # Read the whole file at once
data = binary_file.read()
for i in range(len(data)):
    data[i]=data[i]^137
binary_file =open("secreto.pdf", "wb")
num_bytes_written = binary_file.write(data)
