import os

def shutdown_computer():
    # Use system-specific commands to initiate the shutdown process
    try:
        if os.name == 'nt':  # For Windows
            os.system("shutdown /s /f /t 0")
        elif os.name == 'posix':  # For macOS and Linux
            os.system("sudo shutdown now")
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    shutdown_computer()
