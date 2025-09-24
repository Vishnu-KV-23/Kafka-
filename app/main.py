import socket  # noqa: F401
import struct

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")
    '''
    As a reminder, requests and responses both have the following format:

    1.message_size
    2.Header
    3.Body
    '''
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


    messageSize = 6 #correlationId(4)+apiVersion(2)

    #after waiting for connection the connection is recieved used .recv function
    message=connection.recv(1024)
    print("Recieved request:",message)
    # the request recieved has a header format of

    #HEADER FORMAT
    # message length-x bytes(depends on what all are added in the header
    # apiKey-2 bytes
    # apiVersion- 2 bytes
    # correlationId-4 bytes
    # clientId-variable string

    #so inorder to get correlation id, we have to convert 8th byte to 12th byte from binary to integer...
    # we use struct.unpack for that... >i means ,>-big endian and i means 32 bit integer...
    #struct.unpack always give output as a tuple.. even if there is only one output..(corrId,) form... because usually there is more than one op.. like struct.unpack(">ii", b'\x00\x00\x00\x04\x00\x00\x00\x07') would give (4, 7)


    correlationId=struct.unpack(">i",message[8:12])[0]
    requestApiVersion=struct.unpack(">h",message[6:8])[0]
    if(requestApiVersion>4):
        errorCode=35
    else:
        errorCode=0

    print(f"request API version:{requestApiVersion}")
    print(f"correlationId:{correlationId}")
    print(f"errorCode:{errorCode}")
    response=struct.pack(">iih",messageSize,correlationId,errorCode)
    print(f"response sent:{response}")
    connection.sendall(response)
    print("response sent")


if __name__ == "__main__":
    main()
