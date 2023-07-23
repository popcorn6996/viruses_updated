import os
import shutil
import random
import string

def generate_random_folder_name():
    # Generate a random folder name with 8 characters
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(8))

def create_dummy_folder(folder_path):
    try:
        # Create a dummy folder for demonstration
        os.makedirs(folder_path)
        print(f"Dummy folder '{folder_path}' created.")
    except OSError as e:
        print(f"Error occurred while creating the folder: {e}")

def delete_folder_recursive(folder_path):
    try:
        # Use shutil.rmtree() to recursively delete the folder and its contents
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' has been recursively deleted.")
    except FileNotFoundError:
        print(f"Folder '{folder_path}' does not exist.")
    except OSError as e:
        print(f"Error occurred while deleting the folder: {e}")

if __name__ == "__main__":
    # Predicting a random folder path for deletion
    random_folder_path = os.path.join(os.getcwd(), generate_random_folder_name())

    # Create a dummy folder for demonstration
    create_dummy_folder(random_folder_path)

    # Call the function to recursively delete the folder
    delete_folder_recursive(random_folder_path)
