import socket # Import the socket module for network connections
from concurrent.futures import ThreadPoolExecutor, as_completed # Import ThreadPoolExecutor for multithreading


def portScanner(target, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create TCP socket
        sock.settimeout(0.1) # If no response in 1 second, port is considered closed
        result = sock.connect_ex((target, port)) # Attempt to connect to the target on
        sock.close() # Close the socket
        if result == 0:
            return port
        return None

def portScannerMultithread(target, portStart, portEnd, max_workers=100):
    openPorts = [] # List to store open ports

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(portScanner, target, port): port
            for port in range(portStart, portEnd + 1)
        }

        for future in as_completed(futures): 
            port = future.result() # Get the result of the port scan
            if port is not None: 
                openPorts.append(port) # If port is open, add to list
    return sorted(openPorts) # Return sorted list of open ports

target = input("Enter target IP address: ") # Get target from user
portStart = int(input("Enter starting port number: ")) # Get starting port from user
portEnd = int(input("Enter ending port number: ")) # Get ending port from user
maxThreads = int(input("Enter maximum number of threads (default 100): ") or 100) # Get max threads from user
openPorts = portScannerMultithread(target, portStart, portEnd, maxThreads) # Call the portScanner function
print(f"Open ports on {target}: {openPorts}") # Print the list of open

