import socket
import time

def scan_ports(target_ip, start_port=50, end_port=499):
    print(f"Starting scan on host: {target_ip}")
    open_ports = []

    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # Prevent hanging on closed ports
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: OPEN")
                open_ports.append(port)
    return open_ports

if __name__ == '__main__':
    target = input('Enter the host to be scanned: ')
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        exit(1)

    start_time = time.time()
    scan_ports(target_ip)
    print(f"Time taken: {round(time.time() - start_time, 2)} seconds")
