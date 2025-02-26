def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

file_path = input("Enter the path to the file: ")
data_list = ["Apple"]

write_list_to_file(file_path, data_list)

print(f"The list has been written to {file_path}.")