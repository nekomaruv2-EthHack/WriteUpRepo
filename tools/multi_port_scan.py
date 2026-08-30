import socket
import concurrent.futures
import threading
import argparse
from datetime import datetime

lock = threading.Lock()

def check(target, port, output_file):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, port))
        
        with lock:
            with open(output_file, 'a') as f:
                f.write(f"Open: {port}\n")
        print(f"Open: {port}")
        s.close()
    except:
        pass

# Execute port scan
def execute(target, output_file):
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as ex:
        ex.map(lambda p: check(target, p, output_file), range(1, 65536))

# Generate File name
def generate_file():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f'open_ports_{timestamp}.txt'

def main():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("target", help="target IP address")
    args = parser.parse_args()

    output_file = generate_file()
    print(f"Scanning target: {args.target}, saving to {output_file}")
    
    execute(args.target, output_file)
    print("Scan finished.")

if __name__ == "__main__":
    main()