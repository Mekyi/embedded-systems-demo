# Embedded Systems Demo Project
This project is intended to demo an embedded system with a Raspberry Pi and Sense HAT add-on board. Developed with Python in Raspberry Pi OS (Buster) environment. Also includes an implementation of MQTT client that sends collected data to the cloud.

## Requirements For Running The Project

- Raspberry Pi (with Debian Buster based OS)
- Sense HAT
- Python (>3.7) 

## Sense HAT Sensors

- Gyroscope
- Accelerometer
- Magnetometer
- Temperature
- Barometric pressure
- Humidity

## Running the Demo

Install the Sense Hat software in case it isn't already:

```shell
$ sudo apt-get update
$ sudo apt-get install sense-hat -y
$ sudo reboot
```

Clone this repository:

```shell
$ git clone https://github.com/Mekyi/embedded-systems-demo.git
```

Locate inside the project folder:

```shell
$ cd embedded-systems-demo
```

Install required Python packages:

```shell
$ sudo pip3 install -r requirements.txt
```