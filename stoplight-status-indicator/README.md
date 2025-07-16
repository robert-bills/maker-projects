# Office Stoplight Status System

In early 2017, I transitioned to remote work full time. It didn’t take long to realize the biggest challenge wasn’t bandwidth or productivity—it was people barging in during meetings.

My first solution? A whiteboard on the door.  
My better solution? A custom-built stoplight system with 3D-printed housings, microcontrollers, and a lightweight control GUI.

This project uses a simple UDP-based broadcast protocol to control RGB LEDs housed in 3D-printed “stoplights” around the house.   The controller runs on a small Python GUI, while ESP8266 boards flashed with MicroPython control the lights themselves.  

In true maker fashion, though, my status confirmation still lives on a breadboard on my desk.  

I iterated the design and the code for about a year and a half.  The last major update was somewher in 2019.  
Six years later, it still works beautifully.

---

## What Problem Does This Solve?

- **Visual Do Not Disturb**: A clear, color-coded status at a glance.
- **Network-Simple**: UDP broadcast means zero configuration on the client side.
- **Low-cost, Durable**: Built with off-the-shelf components and a 3D printer.
- **Silent & Respectful**: Prevents interruptions without awkward signs or verbal requests.

---

## How It Works

### Core Technology
- ESP8266 boards flashed with MicroPython
- Python GUI sends UDP messages to update status (`RED`, `YELLOW`, `GREEN`)
- 3D-printed enclosures make the hardware visually friendly

### Transmission
- Lightweight UDP broadcast on the local network
- The message is only a few bytes—perfect for real-time status and low interference

### Hardware
- Standard RGB LED breakout board
- Breadboard and jumper wires
- Power from USB or wall adapter
- 3D-printed housings (see `/images`)

### Software
- `/external-tools/nodemcu-flasher-master.zip`: NodeMCU firmware tool
- `/external-tools/esp8266-20190529-v1.11.bin`: Firmware for ESP8266 MicroPython
- `/external-tools/8266_Flash_Cmd.txt`: Commands for flashing tool firmware

---

## Folder Structure

- `images/` → Photos of the deployed system
- `external-tools/` → NodeMCU flasher utility, firmware, and flash commands
- `designs/` → STL and FreeCAD files for printed components
- `original-code/` → MicroPython code and desktop GUI
- `README.md` → This file

---

## What I'd Do Differently Today

- Swap UDP for MQTT to allow better topic control and remote diagnostics
- Maybe write a mobile client to display the current light status on a widget
- Redesign the case to resemble a traffic signal for fun (and clarity)
- Still use salvaged CAT6 wiring—because I have about a mile of it

---

## Real-World Use

This setup has run continuously since 2019 with very little maintenance. It’s not just a maker toy. It’s infrastructure in my household.

It’s also a great reminder that you don’t need a massive budget or cutting-edge parts to solve real-world problems with elegance and a bit of creativity.

---

## Why This Matters

As a technical educator and builder, I believe good engineering solves problems in context. This project was practical, human-centric, educational for me, and also a hoot to build.

---

## Third-Party Tools and Firmware

This project uses the following open-source components to flash MicroPython to an ESP8266 microcontroller via a Raspberry Pi 3:

### esptool.py
- **Original Repository**: [https://github.com/espressif/esptool](https://github.com/espressif/esptool)
- **License**: GPL-2.0
- **Purpose**: Python-based command-line tool used to flash firmware onto ESP8266 devices.

### MicroPython ESP8266 Firmware
- **Original Source**: [https://micropython.org/download/esp8266/](https://micropython.org/download/esp8266/)
- **License**: MIT
- **Purpose**: Provides a Python runtime on ESP8266 hardware.
- **Note**: The binary included here was downloaded in 2018. Users are encouraged to check for the latest version.

---

## ⚠️ Disclaimer

The firmware and flashing tools included in this repo are for educational and archival purposes only. I do not claim authorship or ownership of these components. Please refer to the original licenses for usage rights and compliance.

---

Feel free to explore, fork, or build your own. If you make a weatherproof version, let me know.

– Rob Bills
