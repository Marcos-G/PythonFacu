with open("secreto.pdf", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    for i in range(256):
        print(i,data[0]^i)
