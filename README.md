# pycom-ftplib
This repository contains an FTP client library for [pycom boards](https://docs.pycom.io/) (MicroPython). It is based on the [micropython-ftplib](https://github.com/SpotlightKid/micropython-ftplib) implementation. Modifications to the `lib/ftplib.py` were done in order to work in the pycom modules. This library was only tested on WiPy 3.0 and FTP_TLS is not fully tested yet.

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
## Usage
To use this library, clone this repository, change `config.json` file with your WiFi and FTP credentials and [program](https://docs.pycom.io/gettingstarted/programming/) all files to the board. 

## LICENSE

Code in file `main.py` and modifications of `lib/ftplib.py` have Copyright (c) of Pablo Zinemanas 2020. This code has the same [Python Software Foundation](https://docs.python.org/3/license.html) License than the original library.
