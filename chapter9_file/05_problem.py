# Write a program to mine a log file and find out whether it contains ‘python’.

# with open("chapter9_file/log.txt") as f :
#     content = f.read()
    
# if("python" in content):
#     print("Word python is presetn in content")
# else:
#     print("The word python is not present ")


# if you have to print line number in which the word in exist

with open("chapter9_file/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes the line is present in content line number is: {lineno } \n")
        break
    line += 1
else:
    print("The line is not present")