import os
import glob
import time

# First of all please please please READ the README.md then start this example.
#
# after booting as root type the following commands
# sudo modprobe w1-gpio
# sudo modprobe w1-therm
#
# Then check /sys/bus/w1/devices/ it has a directory for your device
# with in it you will find w1_slave. It contains the temperature in celsius
# im a european so i don't need to convert it. So we take the raw reading. If need to translate the
# celsius into fahrenheit there is the calculation
#
# temp_f = temp_c * 9.0 / 5.0 + 32.0
#
# If temp_c would be 32 then the end result would be 89,6 fahrenheit
#
# But in my example i will show you the output in celsius.
#
# Credit for reading the temperature goes to youtube user RaspberryPiIVBeginners
# here is his link https://www.youtube.com/channel/UCRAvo5cQWyfog8nRzlf_jWg


base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '00*')[0]  #this is my example this could be 28 or anything realy
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

print read_temp()