import os
import glob
import sys
import time
import serial
import logging
import random
from displayBraille import cells

logging.basicConfig(level=logging.DEBUG)

from pyhaptic import HapticInterface


def find_comm_port():
    comm_port = []
    if os.name == 'posix':
        comm_port = glob.glob('/dev/tty.*')
        comm_port.extend(glob.glob('/dev/ttyACM*'))
        comm_port.extend(glob.glob('/dev/ttyUSB*'))
    elif os.name == 'nt':
        available = []
        for i in range(256):
            try:
                s = serial.Serial('COM' + str(i + 1))
                available.append('COM' + str(i + 1))
                s.close()
            except serial.SerialException:
                pass
        comm_port.extend(available)
    print "Printing current available comm ports.\n"
    for i in comm_port:
        print i
    comm_choice = raw_input(
        "\nPlease choose the full path to the comm port that the haptic controller is connected to:")
    return comm_choice

def send(first, second) :
    print "running " + first
    for x in cells[first]:
        two_d_display.vibrate(x, 0, 0, 1)
        print x
    print "completed " + first
    print "running " + second
    for x in cells[first]:
        two_d_display.vibrate(x + 5, 0, 0, 1)
        print x
    print "completed " + second
    time.sleep(.1)

if __name__ == '__main__':

    two_d_display = HapticInterface(find_comm_port())
    try:
        two_d_display.connect()
    except:
        print "Failed to connect on ..."
        sys.exit(1)

    print "enter a number 0-9 to activate that function"
    print "anything else to exit"
    while True:
        sentence = sys.stdin.read(1)
        sys.stdin.read(1)  # dump the newline char
        i = 0
        while i < len(sentence) :
            send(sentence[i], sentence[i + 1])
            i = i + 2