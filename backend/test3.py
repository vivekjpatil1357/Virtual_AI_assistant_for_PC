import time
from pywifi import PyWiFi, const

def scan_wifi():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  # Assuming the first WiFi interface, change it if you have multiple interfaces
    iface.scan()
    networks = iface.scan_results()
    return networks


