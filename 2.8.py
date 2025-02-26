import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"The file '{file_path}' has been deleted.")
        else:
            print(f"You do not have permission to delete '{file_path}'.")
    else:
        print(f"The file '{file_path}' does not exist.")

file_path = input("Enter the path of the file to delete: ")
delete_file(file_path)