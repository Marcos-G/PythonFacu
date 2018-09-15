with open("secreto.pdf", "rb") as binary_file:
    # Read the whole file at once
    data = binary_file.read()
    print(data)
