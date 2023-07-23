import os
import random
import string

def generate_random_file_name():
    # Generate a random file name with 8 characters
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(8))

def create_dummy_file(file_path):
    try:
        with open(file_path, 'w') as file:
            file.write("This is a dummy file.")

        print(f"Dummy file '{file_path}' created.")
    except Exception as e:
        print(f"Error occurred while creating the dummy file: {e}")

def create_dummy_files_recursively(folder_path, num_files):
    try:
        # Create the main folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Create dummy files in the main folder
        for _ in range(num_files):
            file_name = generate_random_file_name()
            file_path = os.path.join(folder_path, file_name)
            create_dummy_file(file_path)

        # Create dummy files recursively in subdirectories
        for foldername in range(num_files):
            subfolder_path = os.path.join(folder_path, f"subfolder_{foldername}")
            create_dummy_files_recursively(subfolder_path, num_files)

    except Exception as e:
        print(f"Error occurred while creating dummy files recursively: {e}")

if __name__ == "__main__":
    main_folder = input("Enter the name of the main folder: ")
    num_files_per_folder = int(input("Enter the number of dummy files to create in each folder: "))

    create_dummy_files_recursively(main_folder, num_files_per_folder)
