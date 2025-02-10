import requests
from single_sig import pixoo_reset


def main():
    pixoo_reset.reset_display()


    pixoo_url = 'http://iot.digitalag.kr:5000/text'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'text': '출장중입니다',
        'x': '0',
        'y': '20',
        'r': '255',
        'g': '255',
        'b': '255',
        'identifier': '0',
        'font': '1',
        'width': '64',
        'movement_speed': '1',
        'direction': '0'
    }

    response = requests.post(pixoo_url, headers=headers, data=data)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    main()