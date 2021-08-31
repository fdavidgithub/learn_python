# Master
# Send command to blink
import sys

message = '9'
sys.stdout = open("/dev/ttyACM0", 'w')

for m in message:
    sys.stdout.write(m)

