"""
Network setup helper
"""
import network


def wifi_connect():
    """ Connect to a specific wifi network """
    SSID = "YOUR_SSID"
    PASSWORD = "WIFI_PASSWORD"
    DEVICE_HOSTNAME = None

    wifi = network.WLAN(network.STA_IF)
    if not wifi.isconnected():
        print('Connecting to network...')
        wifi.active(True)
        if DEVICE_HOSTNAME:
            wifi.config(dhcp_hostname=DEVICE_HOSTNAME)  # set a hostname for your device, if you wan:
        wifi.connect(SSID, PASSWORD)
        while not wifi.isconnected():
            pass
    print('Network config:', wifi.ifconfig())


def wifi_start_access_point():
    SERVER_SSID = 'myssid'  # max 32 characters
    SERVER_IP = '10.0.0.1'
    SERVER_SUBNET = '255.255.255.0'

    # setup the network
    wifi = network.WLAN(network.AP_IF)
    wifi.active(True)
    wifi.ifconfig((SERVER_IP, SERVER_SUBNET, SERVER_IP, SERVER_IP))
    wifi.config(essid=SERVER_SSID, authmode=network.AUTH_OPEN)
    print('Network config:', wifi.ifconfig())
