import os
from cryptography.fernet import Fernet

def decrypt_folder(source_folder, output_folder, key):
    try:
        # Generate the decryption cipher
        cipher = Fernet(key)

        # Walk through all files and subdirectories in the source folder
        for foldername, _, filenames in os.walk(source_folder):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'rb') as file:
                    encrypted_data = file.read()

                # Decrypt the file data
                decrypted_data = cipher.decrypt(encrypted_data)

                # Create the same folder structure in the output directory
                relative_path = os.path.relpath(file_path, source_folder)
                output_path = os.path.join(output_folder, relative_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                # Write the decrypted data to the output file
                with open(output_path, 'wb') as output_file:
                    output_file.write(decrypted_data)

        print(f"Folder '{source_folder}' decrypted and saved to '{output_folder}'.")
    except Exception as e:
        print(f"Error occurred while decrypting the folder: {e}")

if __name__ == "__main__":
    source_folder = input("Enter the path of the encrypted folder: ")
    output_folder = input("Enter the path for the decrypted folder: ")
    key = input("Enter the encryption key used for decryption: ")

    # Call the function to decrypt the folder
    decrypt_folder(source_folder, output_folder, key.encode('utf-8'))
