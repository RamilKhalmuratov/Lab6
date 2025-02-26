import os

def check_access(path):
    access = {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }
    return access

path = input("Enter the path to check: ")

access_info = check_access(path)

print("\nAccess information:")
print(f"Exists: {access_info['exists']}")
print(f"Readable: {access_info['readable']}")
print(f"Writable: {access_info['writable']}")
print(f"Executable: {access_info['executable']}")