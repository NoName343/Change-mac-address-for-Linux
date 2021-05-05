import subprocess
import random

# writed you mac address
# format 'HV:F3:J7:VF:LS:Z5'
mac = 'DC:F5:05:48:D6:87'

list_mac = [
    '00:89:4F:D9:DA:72', '00:0C:79:30:19:03',
    '00:0C:71:53:40:4F', '00:BA:74:F7:3E:1A',
    '12:E4:4D:E5:F5:19', '12:FA:27:13:4B:81',
    '21:DF:5C:2D:C9:AE', '21:89:ED:79:59:2D'
    ]

def wlan():
    subprocess.call('sudo ifconfig wlan0 down', shell=True)
    subprocess.call(f'sudo ifconfig wlan0 down hw ether {random.choice(list_mac)}', shell=True)
    subprocess.call('sudo ifconfig wlan0 up', shell=True)
    subprocess.call('sudo ifconfig', shell=True)

def eth():
    subprocess.call('sudo ifconfig eth0 down', shell=True)
    subprocess.call(f'sudo ifconfig eth0 down hw ether {random.choice(list_mac)}', shell=True)
    subprocess.call('sudo ifconfig eth0 up', shell=True)
    subprocess.call('sudo ifconfig', shell=True)


subprocess.call('clear', shell=True)
print('your mac: ', mac)
print('1. Wlan0')
print('2. Eth0')
print('3. All')

choice = int(input(': '))
if choice == 1:
    wlan()
if choice == 2:
    eth()
if choice == 3:
    wlan()
    eth()

subprocess.call('sudo ifconfig', shell=True)
subprocess.call('clear', shell=True)
print('Your mac: ', mac)
print('New mac:  ', random.choice(list_mac))
