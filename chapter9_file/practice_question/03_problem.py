import os

os.makedirs("tables", exist_ok=True)

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generateTable(i)
    
    
    
# Algorithm: Generate Multiplication Tables (2 to 20)
# Start.
# Create a function generateTable(n).
# Initialize an empty string table.
# Repeat for i from 1 to 10:
# Calculate n × i.
# Append the result in the format "n X i = n*i" followed by a newline to table.
# Create/open a file named table_n.txt inside the tables folder in write mode.
# Write the contents of table into the file.
# Close the file.
# Repeat steps 2–7 for each number from 2 to 20:
# Call generateTable(number).
# Stop.