import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 9092))
    s.sendall(b"Hello Kafka server!")
    data = s.recv(1024)
    print("Received:", data)
    s.close()

if __name__ == "__main__":
    main()
