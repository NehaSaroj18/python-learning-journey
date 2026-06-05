with open("chapter9_file/old.txt") as f:
    content = f.read()

with open("chapter9_file/renamed_by_python.txt","w") as f:
    f.write(content)  