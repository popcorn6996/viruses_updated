#include <iostream>
#include <Windows.h>

using namespace std;

int main() {
  // Get the current process ID
  DWORD pid = GetCurrentProcessId();

  // Create a shutdown event
  HANDLE shutdownEvent = CreateEvent(NULL, FALSE, FALSE, NULL);

  // Send a restart signal to the system
  SendMessageTimeout(HWND_BROADCAST, WM_SYSCOMMAND, SC_RESTART, 0, SMTO_NORMAL, 1000);

  // Wait for the system to restart
  WaitForSingleObject(shutdownEvent, INFINITE);

  // Exit the program
  return 0;
}
