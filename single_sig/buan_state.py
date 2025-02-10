import requests
import json
import pixoo_reset

def main():
    pixoo_reset.reset_display()


    dashboard_url = 'http://web01.taegon.kr:7500/weather_now/buan'
    dashboard_url2 = 'http://web01.taegon.kr:7500/weather_short/buan'

    response = requests.get(dashboard_url)
    result = response.text
    contents = json.loads(result)
    contents = json.loads(contents)
    temp = contents['ta']
    weather = contents['wwKo']
    # humid = contents['hu']
    time = contents['now_time'].split(' ')[-1]

    response2 = requests.get(dashboard_url2)
    result2 = response2.text
    contents2 = json.loads(result2)
    contents2 = json.loads(contents2)
    humid = contents2[4][f"{contents2[0][0]}"]
    date = contents2[2][0]



    pixoo_url = 'http://web01.taegon.kr:5000/text'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        # 'text': '온실 온습도',
        # 'text': f'{time}',
        # 'text': f'{temp}℃',
        'text': f'{temp}{humid}\n{weather}-부안' + f'\n  {date}\n  {time}',
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