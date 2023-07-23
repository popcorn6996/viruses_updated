import os
from cryptography.fernet import Fernet

def encrypt_folder(source_folder, output_folder, key):
    try:
        # Generate the encryption cipher
        cipher = Fernet(key)

        # Walk through all files and subdirectories in the source folder
        for foldername, _, filenames in os.walk(source_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'rb') as file:
                    data = file.read()

                # Encrypt the file data
                encrypted_data = cipher.encrypt(data)

                # Create the same folder structure in the output directory
                relative_path = os.path.relpath(file_path, source_folder)
                output_path = os.path.join(output_folder, relative_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Write the encrypted data to the output file
                with open(output_path, 'wb') as output_file:
                    output_file.write(encrypted_data)

        print(f"Folder '{source_folder}' encrypted and saved to '{output_folder}'.")
    except Exception as e:
        print(f"Error occurred while encrypting the folder: {e}")

if __name__ == "__main__":
    source_folder = input("Enter the path of the folder you want to encrypt: ")
    output_folder = input("Enter the path for the encrypted folder: ")
    key = Fernet.generate_key()

    # Call the function to encrypt the folder
    encrypt_folder(source_folder, output_folder, key)
