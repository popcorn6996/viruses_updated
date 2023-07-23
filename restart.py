import os

def restart_computer():
    # Use system-specific commands to initiate the restart process
    try:
        if os.name == 'nt':  # For Windows
            os.system("shutdown /r /f /t 0")
        elif os.name == 'posix':  # For macOS and Linux
            os.system("sudo shutdown -r now")
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    restart_computer()
