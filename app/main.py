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
    # generated documentation from chatgpt in case... i forget...

    #must import STRUCT before using struct.pack


    # Build the Kafka response header:
    # We must send 2 integers in binary form:
    #   1. message_size (4 bytes, here set to 0)
    #   2. correlation_id (4 bytes, here set to 7)
    #
    # struct.pack(">ii", message_size, correlationId) converts these Python ints to bytes.
    # Format string breakdown:
    #   ">"  = big-endian (network byte order, most significant byte first)
    #   "i"  = one 32-bit signed integer (4 bytes)
    #   "ii" = two 32-bit signed integers in sequence
    #
    # So ">ii" means: "encode two 4-byte signed ints in big-endian order".
    # Example:
    #   message_size = 0 → 00 00 00 00
    #   correlationId = 7 → 00 00 00 07
    # Together: 00 00 00 00 00 00 00 07

    correlationId = 7
    messageSize = 4

    #after waiting for connection the connection is recieved used .recv function
    connection.recv(1024)
    print("Recieved request")

    response=struct.pack(">ii",messageSize,correlationId)
    print(f"response sent:{response}")
    connection.sendall(response)
    print("response sent")


if __name__ == "__main__":
    main()
