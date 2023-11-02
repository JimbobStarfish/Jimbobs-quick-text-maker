print("Welcome To the quick text typer, type to begin!")
text = input("type here: ")
Make = input("Do you want to make the file? (Y/N): ")

if Make == 'Y':
    with open('output_file.txt', 'w') as file:
        file.write(text)
    print("File created successfully!")
else:
    print("File creation skipped.")