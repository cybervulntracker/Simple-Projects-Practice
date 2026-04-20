# Simple Port Scanner in Python
# This script checks which ports are open on a target host
# Good for beginners learning networking basics

import socket  # Built-in library for networking

# Ask the user to enter a target (IP address or website)
target = input("Enter target IP or domain (e.g., google.com): ")

# Convert domain name to IP (if user enters a website)
try:
    target_ip = socket.gethostbyname(target)
    print(f"\nScanning target: {target} ({target_ip})\n")
except socket.gaierror:
    print("Invalid hostname. Please try again.")
    exit()

start_port = 1
end_port = 100

# Loop through each port in the range
for port in range(start_port, end_port + 1):
    # Create a new socket for each port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout so it doesn't hang forever
    s.settimeout(0.5)
    
    # Try connecting to the port
    result = s.connect_ex((target_ip, port))
    
    # connect_ex returns 0 if the connection was successful
    if result == 0:
        print(f"Port {port} is OPEN")
    
    # Close the socket after checking
    s.close()

print("\nScan complete!")