# Open the original file and create a new file for formatted output
with open('modulelist.txt', 'r', encoding='utf-8') as input_file, open('formattedlist2.txt', 'w', encoding='utf-8') as output_file:
    for line in input_file:
        if line.strip():  # Check if the line is not empty
            output_file.write(line)  # Write non-empty lines to the new file

print("Blank lines removed and written to formattedlist.txt")
