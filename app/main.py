import socket  # noqa: F401
import struct

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection,address= server.accept() # wait for client
    print("Connection object",connection)
    print("Address:ip address and port",address)
    #LEVEL 2
    correlationId = 7
    messageSize = 4


    connection.recv(1024)
    print("Recieved request")
    response=struct.pack(">ii",messageSize,correlationId)
    print(f"response sent:{response}")
    connection.sendall(response)
    print("response sent")


if __name__ == "__main__":
    main()
