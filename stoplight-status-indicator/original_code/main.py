red = machine.Pin(16, machine.Pin.OUT)
yellow = machine.Pin(5, machine.Pin.OUT)
green = machine.Pin(4, machine.Pin.OUT)

for item in (red, yellow, green):
    item.off()

while True:
    color = "Green"
    new_color = 'Enter a color: (Red, Yellow, Green, Quit)'
    while str.lower(new_color) != "quit":
        color.off()
        color = new_color
        color.on()
    else:
        print("Please enter Red, Yellow or Green. (Quit to exit)")
        