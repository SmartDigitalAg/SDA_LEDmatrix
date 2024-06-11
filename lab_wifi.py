
import requests
import pyqrcode as pq
import pixoo_reset
from requests_toolbelt.multipart.encoder import MultipartEncoder

def set_wifi():
    # ssid = input("와이파이 이름을 입력해주세요: ")
    # security = input("Security: ")
    # password = input("Password: ")
    # ssid = 'SmartDigitalAgLab'
    # security = 'WPA'
    # password = 'Smartfarm208!'
    ssid = 'SmartDigitalAgLab_Guest'
    security = 'WPA'
    password = 'abc123@sda'

    qr = pq.create(f'WIFI:T:{security};S:{ssid};P:{password};;')
    qr.png('wifi_connect_home.png', scale=8)

def main():
    pixoo_reset.reset_display()
    set_wifi()

    pixoo_url = 'http://web01.taegon.kr:5000/image'

    with open('wifi_connect_home.png', 'rb') as file:
        m = MultipartEncoder(
            fields={
                'image': ('wifi_connect_home.png', file, 'image/png'),
                'x': '0',
                'y': '0',
                'push_immediately': 'true'
            }
        )

        response = requests.post(
            pixoo_url,
            data=m,
            headers={'Content-Type': m.content_type}
        )



    print(response.text)

    if response.status_code == 200:
        print('success')
    else:
        print('fail')



if __name__ == '__main__':
    main()
