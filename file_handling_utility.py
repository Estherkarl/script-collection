
import os

# Function to list files in a directory
def list_files(directory):
    files = os.listdir(directory)
    return files

# Function to create a new directory
def create_directory(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

# Example usage
if __name__ == "__main__":
    # List files in current directory
    current_directory_files = list_files('.')
    print(f"Files in current directory: {current_directory_files}")

    # Create a new directory
    new_directory_name = 'new_directory'
    create_directory(new_directory_name)
