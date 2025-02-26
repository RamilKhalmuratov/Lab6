import os

def check_path_and_extract_info(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        return True, directory, filename
    return False, None, None

path = input("Enter the path to check: ")

exists, directory, filename = check_path_and_extract_info(path)

if exists:
    print(f"\nThe path exists.")
    print(f"Directory: {directory}")
    print(f"Filename: {filename}")
else:
    print("\nThe path does not exist.")