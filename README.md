# pycom-ftplib
This repository contains An FTP client library for pycom boards (MicroPython). It is based in the [micropython-ftplib](https://github.com/SpotlightKid/micropython-ftplib) implementation. Modifications were done in order to work in the pycom modules, thought the library was only tested on WiPy 3.0. FTP_TLS is not yet fully tested. 

## Organization of this repository 

````
root/
|
|- lib/ _______________________________ # Firmware source files
|  |- ftplib.py _______________________ # ftplib adapted to pycom modules
|
|- main.py ____________________________ # Example of main program that includes several tests.
|- config.json ________________________ # Configuration file (WiFi and FTP parameters)
|
````
