import tkinter as tk
from socket import *
import threading
import time

UDP_IP_ADDRESS = '255.255.255.255'
UDP_PORT_NO = 9999
clientSock = socket(AF_INET, SOCK_DGRAM)
clientSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
clientSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


def broadcast_color(message):
    t = threading.current_thread()
    while getattr(t, "do_run" , True):
        clientSock.sendto(message, (UDP_IP_ADDRESS, UDP_PORT_NO))
        time.sleep(5)

def kill_lights():
    for t in threading.enumerate():
        t.do_run = False

        
def red_light():
    kill_lights()
    message = b'red'
    # broadcast_color(message)
    m_thread = threading.Thread(target=broadcast_color, args=(message, ))
    m_thread.start()
    # clientSock.sendto(message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    label.configure(text="Current color: Red", bg="red")


def yellow_light():
    kill_lights()
    message = b'yellow'
    # broadcast_color(message)
    m_thread = threading.Thread(target=broadcast_color, args=(message, ))
    m_thread.start()
    # clientSock.sendto(message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    label.configure(text="Current color: Yellow", bg="yellow")


def green_light():
    kill_lights()
    message = b'green'
    # broadcast_color(message)
    m_thread = threading.Thread(target=broadcast_color, args=(message, ))
    m_thread.start()
    # clientSock.sendto(message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    label.configure(text="Current color: Green", bg="green")


def light_off():
    kill_lights()
    message = b'off'
    # broadcast_color(message)
    m_thread = threading.Thread(target=broadcast_color, args=(message, ))
    m_thread.start()
    # clientSock.sendto(message, (UDP_IP_ADDRESS, UDP_PORT_NO))
    label.configure(text="Current color: Off", bg="light gray")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Office Lights")
    frame = tk.Frame(root)
    frame.pack(padx=2, pady=2)
    label = tk.Label(frame,
                     width=50,
                     text="Current color:")
    label.pack()
    button = tk.Button(frame,
                       bg="red",
                       height=10,
                       width=50,
                       command=red_light)
    button.pack(side=tk.TOP)
    button = tk.Button(frame,
                       bg="yellow",
                       height=10,
                       width=50,
                       command=yellow_light)
    button.pack()
    button = tk.Button(frame,
                       bg="green",
                       height=10,
                       width=50,
                       command=green_light)
    button.pack()
    button = tk.Button(frame,
                       text="Lights off",
                       height=5,
                       width=50,
                       command=light_off)
    button.pack(side=tk.BOTTOM)
    root.mainloop()
    kill_lights()
