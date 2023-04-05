from bluetooth import *
import pandas as pd

print("Scanning for bluetooth devices... ")
devices = discover_devices(lookup_names = True, lookup_class=True)
number_of_devices = len(devices)

print(number_of_devices, "Devices found")
device_format = pd.DataFrame.from_records(data=devices, columns=["MAC address", "Dev1ce name", "Device Class"])
for device in devices:
    print(device_format)

services = find_service(None,None,"localhost")
print("Number of services:",len(services))
if len(services) == 0:
    print("No services found!")
else:
    print("Services Found")
    print("\n")
    for serv in services:
        print("  Service name:",serv['name'])
        print("  Host: ", serv["host"])
        print("  Description: ", serv["description"])
        print("  Provided By: ", serv["provider"])
        print("  Protocol: ", serv["protocol"])
        print("  Channel/PSM: ", serv["port"])
        print("  Service Classes: ", serv["service-classes"])
        print("  Profiles:" ,serv["profiles"] )
        print("  Service ID: ", serv["service-id"])
        print("\n")           
    print("\n")