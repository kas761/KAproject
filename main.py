with open('data.txt', 'r') as file:
        content = file.read()
        lines = file.readlines()
        for line in file:
            print(line)  
        
line_count = len(lines)
print(f"Number of lines in the file: {line_count}")