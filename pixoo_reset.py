import requests

def reset_display():
    pixoo_reset = 'http://iot.digitalag.kr:5000/fill'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'r': '0',
        'g': '0',
        'b': '0'
    }

    requests.post(pixoo_reset, headers=headers, data=data)