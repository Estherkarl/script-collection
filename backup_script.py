import os
import shutil

def backup_files(source_directory, destination_directory):
    try:
        # Check if source directory exists
        if not os.path.exists(source_directory):
            print(f"Error: Source directory '{source_directory}' does not exist.")
            return
        
        # Create destination directory if it doesn't exist
        os.makedirs(destination_directory, exist_ok=True)
        
        # Iterate over files and subdirectories in the source directory
        for item in os.listdir(source_directory):
            source_item = os.path.join(source_directory, item)
            destination_item = os.path.join(destination_directory, item)
            
            # Recursively copy if item is a directory
            if os.path.isdir(source_item):
                shutil.copytree(source_item, destination_item, dirs_exist_ok=True)
            else:
                shutil.copy2(source_item, destination_item)  # Copy file
            
            print(f"Copied '{source_item}' to '{destination_item}'")
        
        print("Backup completed successfully!")
    
    except Exception as e:
        print(f"An error occurred during backup: {str(e)}")

# Example usage
if __name__ == "__main__":
    source_directory = '/home/dci-student/script-collection/reports'
    destination_directory = '/home/dci-student/script-collection/Backup'
    backup_files(source_directory, destination_directory)
