
with open("text.txt", "r") as f:
    content = f.read()

words = content.split()  


modified_words = ["+" + word for word in words]

new_content = " ".join(modified_words)

with open("text.txt", "w") as f:
    f.write(new_content)