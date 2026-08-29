import socket
import concurrent.futures
import threading

target = '172.20.0.52'
output_file = 'open_ports.txt'
lock = threading.Lock()

def check(port):
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

with concurrent.futures.ThreadPoolExecutor(max_workers=500) as ex:
    ex.map(check, range(1, 65536))

print("Scan finished.")