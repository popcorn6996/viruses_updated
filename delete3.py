import os

def delete_folder(folder_path):
    try:
        # Check if the folder exists before attempting to delete
        if os.path.exists(folder_path):
            # Use os.rmdir() to remove the directory if it's empty
            os.rmdir(folder_path)
            print(f"Folder '{folder_path}' has been deleted.")
        else:
            print(f"Folder '{folder_path}' does not exist.")
    except OSError as e:
        print(f"Error occurred while deleting the folder: {e}")

if __name__ == "__main__":
    for _ in range(3):
        folder_to_delete = input("Enter the path of the folder you want to delete: ")

        # Call the function to delete the folder
        delete_folder(folder_to_delete)
