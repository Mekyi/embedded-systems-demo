# Embedded Systems Demo Project
This project is intended to demo an embedded system with a Raspberry Pi and Sense HAT add-on board. Developed with Python in Raspberry Pi OS (Buster) environment. Also includes an implementation of MQTT client that sends collected data to the cloud.

## Requirements For Running The Project

- Raspberry Pi (with Debian Buster based OS)
- Sense HAT
- Python3-venv (virtual environment)

## Sense HAT Sensors

- Gyroscope
- Accelerometer
- Magnetometer
- Temperature
- Barometric pressure
- Humidity

## Running the Demo

Install the Python3-venv package

```shell
$ sudo apt-get install python3-venv -y
```

Clone this repository to your Raspberry Pi

```shell
$ git clone https://github.com/Mekyi/embedded-systems-demo.git
```

Locate inside the project folder:

```shell
$ cd embedded-systems-demo
```

### Activating the virtual environment

Activates virtual environment. If virtual environment doesn't already exist, it is created with required packages:

```shell
$ source activate
```

## Package management

List installed packages:

```shell
(python3-virtualenv) $ pip list
```

Installing requirements manually. This is done automatically when activating the virtual environment for the first time:

```shell
(python3-virtualenv) $ pip install -r requirements.txt
```

Saving list of installed packages in the requirements.txt file:

```shell
(python3-virtualenv) $ pip freeze > requirements.txt
```

Installing new packages:

```shell
(python3-virtualenv) $ pip install <package name>
```

### Deactivating the virtual environment

```shell
(python3-virtualenv) $ deactivate
```
