import os
import zipfile
import shutil

def encrypt_folder(source_folder, output_zip, password):
    try:
        # Create a ZIP file with the specified password
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through all files and subdirectories in the source folder
            for foldername, subfolders, filenames in os.walk(source_folder):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    # Add each file to the ZIP file with encryption
                    zipf.write(file_path, os.path.relpath(file_path, source_folder), zipfile.ZIP_AES_128, pwd=password.encode('utf-8'))

        print(f"Folder '{source_folder}' encrypted and saved to '{output_zip}'.")
    except Exception as e:
        print(f"Error occurred while encrypting the folder: {e}")

if __name__ == "__main__":
    source_folder = input("Enter the path of the folder you want to encrypt: ")
    output_zip = input("Enter the path for the encrypted ZIP file (with .zip extension): ")
    password = input("Enter the password for encryption: ")

    # Call the function to encrypt the folder
    encrypt_folder(source_folder, output_zip, password)
