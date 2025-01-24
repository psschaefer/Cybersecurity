import socket
import psutil
import time
import numpy as np
import Cybersecurity.Plotter as Plotter

# monitor memory and cpu
def monitor_capacity():
    current_time_step = 0

    while True:

        cpu_usage = psutil.cpu_percent(interval=0.1)
        memory_usage = psutil.virtual_memory().percent
        current_time_step += 0.1

        cpu = np.append(cpu, int(cpu_usage))
        memory = np.append(memory, int(memory_usage))
        time_steps = np.append(time_steps, current_time_step)

        time.sleep(0.1)

        if current_time_step > 15:
            break

# define globals
host = '10.0.0.55' # '10.0.0.251'
port = 25

time_steps = np.array([])
memory = np.array([])
cpu = np.array([])

# listen for smtp connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"SMTP server listening on {host}:{port}...")

try:
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}, start monitoring...")
        monitor_capacity()
except KeyboardInterrupt:
    print("Shutting down SMTP server.")
finally:
    server_socket.close()

Plotter.plot(time_steps, memory, cpu)
