import hashlib

filename = input("Enter file path: ")

sha256 = hashlib.sha256()

try:
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    print("SHA256 Hash:")
    print(sha256.hexdigest())

except FileNotFoundError:
    print("File not found.")