import os

def list_contents(path):
    files = []
    directories = []
    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

    return directories, files

path = input("Enter the directory path: ")

if os.path.exists(path):
    directories, files = list_contents(path)
    print("\nDirectories:")
    print("\n".join(directories) if directories else "None")

    print("\nFiles:")
    print("\n".join(files) if files else "None")

    print("\nAll contents:")
    print("\n".join(directories + files))
else:
    print("Invalid path! Please enter a valid directory.")