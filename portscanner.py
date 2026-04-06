import socket
import threading
from queue import Queue

# Target host (change this to whatever you want to scan)
target = "127.0.0.1"

# Number of threads (more threads = faster scan, but too many can overwhelm your system)
NUM_THREADS = 50

# Queue to hold ports that need to be scanned
port_queue = Queue()

# Lock for clean output (so threads don't print over each other)
print_lock = threading.Lock()


def scan_port(port):
    """
    Try connecting to a port.
    If connection succeeds, port is open.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Timeout so it doesn't hang forever on closed ports
        sock.settimeout(1)

        # Attempt to connect
        result = sock.connect_ex((target, port))

        # If result is 0, connection worked → port is open
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} is OPEN")

        sock.close()

    except Exception as e:
        # Not printing every error keeps output clean
        pass


def worker():
    """
    Worker thread:
    Keeps taking ports from queue and scanning them.
    """
    while True:
        port = port_queue.get()

        # Scan the port
        scan_port(port)

        # Mark this task as done so queue knows progress
        port_queue.task_done()


def main():
    print(f"Starting scan on {target}...\n")

    # Create worker threads
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker)

        # Daemon threads exit when main program exits
        t.daemon = True
        t.start()

    # Add ports to the queue (example: scan first 1024 ports)
    for port in range(1, 1025):
        port_queue.put(port)

    # Wait until all ports are processed
    port_queue.join()

    print("\nScan completed.")


if __name__ == "__main__":
    main()