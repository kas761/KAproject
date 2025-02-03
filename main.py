with open('data.txt', 'r') as file:
    content = file.read()
    line_count = content.count('\n') + 1
    char_count = len(content)

print(f'The number of lines in the file is: {line_count} and number of characters is: {char_count}')