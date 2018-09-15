with open("secreto.pdf", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    for i in range(len(data)):
        data[i]=data[i]^137
    num_bytes_written = binary_file.write(data)
    print("Wrote %d bytes." % num_bytes_written)
