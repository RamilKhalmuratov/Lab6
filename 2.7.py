def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(contents)
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"The file '{source_file}' does not exist.")
    except IOError as e:
        print(f"An error occurred: {e}")

source_file_path = input("Enter the path of the source file: ")
destination_file_path = input("Enter the path of the destination file: ")

copy_file_contents(source_file_path, destination_file_path)