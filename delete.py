import shutil

def delete_folder(folder_path):
    try:
        # Use the shutil.rmtree function to delete the folder and its contents
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_path = r'C:\Users\USER\Desktop\testfolder'  # Replace with the actual folder path
    delete_folder(folder_path)
