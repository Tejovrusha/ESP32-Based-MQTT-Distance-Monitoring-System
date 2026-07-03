# ESP32-Based MQTT Distance Monitoring System

## Overview

This project demonstrates a simple IoT distance monitoring system using an ESP32 microcontroller, an HC-SR04 ultrasonic sensor, and the MQTT messaging protocol.

The ESP32 measures the distance to an object using the HC-SR04 sensor and publishes the measured value to an MQTT broker over Wi-Fi whenever the distance changes. This minimizes unnecessary network traffic while providing real-time sensor updates to any MQTT subscriber.

---

## Features

* Real-time distance measurement using the HC-SR04 ultrasonic sensor
* Wi-Fi connectivity using the ESP32
* MQTT-based wireless communication
* Publishes data only when the measured distance changes
* Lightweight and suitable for IoT applications
* Modular code with a dedicated distance measurement function

---

## Hardware Requirements

* ESP32 Development Board
* HC-SR04 Ultrasonic Sensor
* Jumper Wires
* USB Cable
* Wi-Fi Network

---

## Software Requirements

* MicroPython
* Thonny IDE (or any MicroPython IDE)
* Mosquitto MQTT Broker
* `umqtt.simple` library

---

## Circuit Connections

| HC-SR04 | ESP32   |
| ------- | ------- |
| VCC     | 5V      |
| GND     | GND     |
| TRIG    | GPIO 23 |
| ECHO    | GPIO 32 |

---

## MQTT Configuration

Configure the following variables before running the program:

```python
MQTT_CLIENT = "esp32"
MQTT_BROKER = "YOUR_BROKER_IP"
MQTT_TOPIC = "sensor/distance"
```

Replace `YOUR_BROKER_IP` with the IP address of your MQTT broker.

Example:

```
192.168.1.45
```

---

## Wi-Fi Configuration

Update the Wi-Fi credentials in the program:

```python
sta_if.connect("YOUR_WIFI_NAME", "YOUR_PASSWORD")
```

---

## Working Principle

1. The ESP32 connects to the local Wi-Fi network.
2. It establishes a connection with the MQTT broker.
3. The HC-SR04 measures the distance to an object.
4. The ESP32 compares the current reading with the previously published value.
5. If the distance has changed, the new value is published to the MQTT topic.
6. The process repeats every second.

---

## MQTT Topic

```
sensor/distance
```

Example published payload:

```
25.43
```

---

## Project Workflow

```
Power On
    │
    ▼
Connect to Wi-Fi
    │
    ▼
Connect to MQTT Broker
    │
    ▼
Measure Distance
    │
    ▼
Distance Changed?
   ┌───────┐
   │       │
  No      Yes
   │       │
   │   Publish Reading
   │       │
   └──► Wait 1 Second
           │
           ▼
        Repeat
```

---

## Technologies Used

* ESP32
* MicroPython
* MQTT
* Mosquitto MQTT Broker
* HC-SR04 Ultrasonic Sensor
* Wi-Fi Networking

---

## Future Improvements

* Add automatic MQTT reconnection after network failures.
* Publish sensor readings in JSON format.
* Add timestamp support.
* Support multiple sensors.
* Implement QoS and retained MQTT messages.
* Add secure MQTT communication using TLS authentication.

---

## Learning Outcomes

Through this project, the following concepts were implemented and understood:

* MQTT publish architecture
* ESP32 Wi-Fi programming
* MQTT client configuration
* Ultrasonic distance measurement
* GPIO programming with MicroPython
* Basic IoT system design
