import requests
import json
import pixoo_reset

def main():
    pixoo_reset.reset_display()

    dashboard_url = 'http://web01.taegon.kr:7600/test'
    response = requests.get(dashboard_url)
    result = response.text
    result = json.loads(result)
    temp = result['grh']['day_temp'][-1]
    humid = result['grh']['day_humid'][-1]
    time = result['grh']['day_time'][-1]
    date = result['grh']['date'][-1]
    date_str = f"{date.split('-')[1]}/{date.split('-')[2]}"


    pixoo_url = 'http://web01.taegon.kr:5000/text'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        # 'text': '온실 온습도',
        # 'text': f'{time}',
        # 'text': f'{temp}℃',
        'text': f'{temp}℃  \n{humid}%\n        {date_str}\n{time}\n 온실',
        'x': '3',
        'y': '0',
        'push_immediately': 'true'

    }

    response = requests.post(pixoo_url, headers=headers, data=data)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    main()