with open("chapter9_file/this.txt") as f:
    content = f.read()

with open("chapter9_file/this_copy.txt", "w") as f:
    f.write(content)
