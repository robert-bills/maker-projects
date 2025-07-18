# Again we import the necessary socket python module
import socket
import machine
# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = ''
UDP_PORT_NO = 9999

green_pin = machine.Pin(4, machine.Pin.OUT)
yellow_pin = machine.Pin(5, machine.Pin.OUT)
red_pin = machine.Pin(15, machine.Pin.OUT)

# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
current = green_pin
def clear_light(current_pin):
    current_pin.off()
    
if __name__ == "__main__":
    while True:
        data, addr = serverSock.recvfrom(1024)
        # print("Message: ", data)
        if data == b'green':
            # print("Light is green")
            clear_light(current)
            green_pin.on()
            current = green_pin
        elif data == b'yellow':
            # print("Light is yellow")
            clear_light(current)
            yellow_pin.on()
            current = yellow_pin
        elif data == b'red':
            # print("Light is red")
            clear_light(current)
            red_pin.on()
            current = red_pin
        elif data == b'off':
            clear_light(current)
