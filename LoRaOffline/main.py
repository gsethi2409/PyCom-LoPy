from network import LoRa
import socket
import machine
import time
import binascii

print('Initializing')
time.sleep(2)
# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORA, frequency=867500000, tx_power=14, bandwidth=LoRa.BW_125KHZ,sf=7)

print('Creating raw LoRa socket')
time.sleep(2)
# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

print('Before loop')
while True:
    # send some data
    s.setblocking(True)
    s.send('HI')
    print("!Sending!")
    time.sleep(machine.rng() & 0x0F)