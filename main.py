from machine import Pin, time_pulse_us
import network
import time
from umqtt.simple import MQTTClient

MQTT_CLIENT="esp32"
MQTT_BROKER="YOUR_BROKER_IP"
MQTT_TOPIC="sensor/distance" 

trigger=Pin(23, Pin.OUT)
echo=Pin(32, Pin.IN)
trigger.value(0)
time.sleep_us(5)
prev_dist=""

print("Connecting to WiFi",end="")
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('freeWifi','password')
while not sta_if.isconnected():
  print(".",end="")
  time.sleep(0.1)
print("\nConnected!")

print("Connecting to MQTT server...",end="")
client=MQTTClient(MQTT_CLIENT, MQTT_BROKER)
client.connect()
print("Connected!")

def get_distance():
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    duration=time_pulse_us(echo,1,50000)
    if duration<0:
        return -1
    return f'{(duration*0.0343)/2:.2f}'

try:
    while True:
      current_dist=get_distance()
      if current_dist==-1:
          continue
      if current_dist!=prev_dist:
        client.publish(MQTT_TOPIC, str(current_dist))
        prev_dist=current_dist
      time.sleep(1)
except:
    print("Disconnected")
