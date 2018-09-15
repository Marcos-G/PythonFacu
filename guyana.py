with open("secreto.pdf", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data[0],data[0]^1,data[0]^2,data[0]^3)
