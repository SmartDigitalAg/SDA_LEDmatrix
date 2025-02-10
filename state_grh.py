import requests
import json
import pixoo_reset

def main():
    pixoo_reset.reset_display()


    dashboard_url = 'http://iot.digitalag.kr:7600/recent'
    response = requests.get(dashboard_url)
    result = response.text
    result = json.loads(result)
    temp = result['grh']['temperature']
    humid = result['grh']['humidity']

    date = result['grh']['timestamp']
    date_str = f"{date.split('-')[1]}/{date.split('-')[2]}"
    time_str = f"{date.split(' ')[1][0:5]}"


    pixoo_url = 'http://iot.digitalag.kr:5000/text'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'text': f'온실  \n {time_str}\n 온도   {temp}℃\n 습도   {humid}%',
        'x': '0',
        'y': '0',
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