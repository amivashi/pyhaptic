import os
import glob
import sys
import time
import serial
import logging
import random
from displayBraille import cells
from displayBraille import freq

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
    return comm_port[0]

def send(first, second) :
    print "running " + first
    try:
        frequency = freq[first]
        print "frequency " + str(frequency)
        for x in cells[first]:
            #two_d_display.vibrate(x, 0, 0, frequency)
            print x
    except:
        print "Symbol Not Found"
    try:
        print "completed " + first
        print "running " + second
        frequency = freq[second]
        print "frequency " + str(frequency)
        for x in cells[second]:
            #two_d_display.vibrate(x + 5, 0, 0, frequency)
            print x
    except:
        print "Symbol Not Found"
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

def recieve_content(input_data) :
    try:
        two_d_display = HapticInterface(find_comm_port())
        two_d_display.connect()
    except:
        print "Failed to connect on ..."
    i = 0
    while i < len(input_data):
        try:
            send(input_data[i], input_data[i + 1])
            i = i + 2
        except:
            print "Length out of bound"
            send(input_data[i], " ")
            i = i + 2