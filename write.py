with open("text.txt", "a+") as f:
    f.write("New line\n")
    f.seek(0)
    print(f.read())