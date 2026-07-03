# ESP32 MQTT Distance Monitoring System

## Setup & Installation Guide

This guide explains how to set up the complete environment required to run the project.

---

# Step 1: Install Mosquitto

1. Download the latest Mosquitto installer for Windows (64-bit if your system is 64-bit).
2. Run the installer.
3. Complete the installation using the default options.
4. Note the installation directory (typically):

```
C:\Program Files\Mosquitto
```

---

# Step 2: Open Command Prompt

Open Command Prompt and navigate to the Mosquitto installation directory.

```
cd "C:\Program Files\Mosquitto"
```

---

# Step 3: Verify the Installation

Run:

```
mosquitto -h
```

If installed correctly, Mosquitto will display its help information.

---

# Step 4: Create a Configuration File

Create a file named:

```
mosquitto.conf
```

Add the following contents:

```
listener 1883
allow_anonymous true
```

This allows devices on the local network to connect to the broker.

> Note:
> If you already have a configuration file, edit it instead of creating a new one.

---

# Step 5: Start the MQTT Broker

Run:

```
mosquitto -c mosquitto.conf -v
```

If successful, you should see output similar to:

```
Opening ipv4 listen socket on port 1883
Opening ipv6 listen socket on port 1883
mosquitto version 2.x running
```

Leave this Command Prompt window open.

The broker must continue running while the ESP32 is publishing data.

---

# Step 6: Find the Broker IP Address

Open another Command Prompt.

Run:

```
ipconfig
```

Locate your Wi-Fi adapter.

Example:

```
IPv4 Address . . . . . . . : 192.168.1.45
```

Use this address in your ESP32 code:

```python
MQTT_BROKER = "192.168.1.45"
```

Replace it with your own IPv4 address if it is different.

---

# Step 7: Connect the ESP32

Connect the ESP32 to your computer using a USB cable.

Open Thonny IDE.

Select:

```
Interpreter
↓

MicroPython (ESP32)
```

---

# Step 8: Configure Wi-Fi

Update your Wi-Fi credentials:

```python
sta_if.connect("YOUR_WIFI_NAME", "YOUR_WIFI_PASSWORD")
```

Example:

```python
sta_if.connect("HomeWiFi", "mypassword")
```

The ESP32 and the computer running Mosquitto must be connected to the same Wi-Fi network.

---

# Step 9: Upload the Program

Save the Python program to the ESP32 as:

```
main.py
```

or run it directly from Thonny.

---

# Step 10: Run an MQTT Subscriber

Open another Command Prompt.

Navigate to the Mosquitto directory:

```
cd "C:\Program Files\Mosquitto"
```

Run:

```
mosquitto_sub -h 192.168.1.45 -t sensor/distance
```

Replace the IP address with your computer's IPv4 address if necessary.

The subscriber is now waiting for messages.

---

# Step 11: Run the ESP32 Program

Run the MicroPython program.

The ESP32 will:

1. Connect to Wi-Fi.
2. Connect to the MQTT broker.
3. Measure the distance.
4. Publish the value whenever it changes.

The subscriber terminal should display values similar to:

```
25.34
26.01
31.75
18.42
```

---

# Useful MQTT Commands

## Start Broker

```
mosquitto -c mosquitto.conf -v
```

---

## Subscribe to a Topic

```
mosquitto_sub -h 192.168.1.45 -t sensor/distance
```

---

## Subscribe to All Sensor Topics

```
mosquitto_sub -h 192.168.1.45 -t sensor/#
```

---

## Publish a Test Message

```
mosquitto_pub -h 192.168.1.45 -t sensor/distance -m "50"
```

---

## Publish to Another Topic

```
mosquitto_pub -h 192.168.1.45 -t sensor/status -m "Online"
```

---

## Stop the Broker or Subscriber

Press:

```
Ctrl + C
```

---

# Troubleshooting

### Wi-Fi does not connect

* Verify the SSID and password.
* Ensure the ESP32 is within Wi-Fi range.

---

### MQTT connection fails

* Verify the broker IP address.
* Ensure Mosquitto is running.
* Confirm both the ESP32 and computer are connected to the same Wi-Fi network.

---

### "Starting in local only mode"

The broker is configured to accept only local connections.

Ensure the configuration file contains:

```
listener 1883
allow_anonymous true
```

Restart Mosquitto after making changes.

---

### Port 1883 already in use

Another Mosquitto instance or service is already running.

Check:

```
netstat -ano | findstr :1883
```

Identify the process:

```
tasklist /FI "PID eq <PID>"
```

Stop the existing service if required before starting a new broker.

---

# Project Architecture

```
HC-SR04
    │
    ▼
ESP32 Publisher
    │
 Wi-Fi Network
    │
    ▼
MQTT Broker (Mosquitto)
    │
    ▼
MQTT Subscriber
    │
Displays Distance
```

The MQTT broker acts as the intermediary between publishers and subscribers. The ESP32 only publishes data to the broker and does not communicate directly with subscribers.
