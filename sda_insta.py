import requests
import pixoo_reset

def main():
    pixoo_reset.reset_display()

    url = 'http://web01.taegon.kr:5000/bigqrcode'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'site url': 'https://www.instagram.com/sda_lab/',
        'x': '0',
        'y': '0',
        'push_immediately': 'true',
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    main()