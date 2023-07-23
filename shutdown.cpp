
#include <cstdlib> // For the system function

int main() {
    // Use system-specific commands to initiate the shutdown process
#ifdef _WIN32 // For Windows
    system("shutdown /s /f /t 0");
#elif __APPLE__ // For macOS
    system("sudo shutdown -h now");
#elif __linux__ // For Linux
    system("sudo shutdown now");
#else
    #error Unsupported operating system
#endif

    return 0;
}
