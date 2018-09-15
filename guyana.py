with open("secreto.pdf", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data[0]^137,data[1]^137,data[2]^137,data[3]^137)
