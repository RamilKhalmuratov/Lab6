def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return None

file_path = input("Enter the path to the text file: ")
line_count = count_lines_in_file(file_path)

if line_count is not None:
    print(f"The number of lines in the file is: {line_count}")
else:
    print("The specified file does not exist.")