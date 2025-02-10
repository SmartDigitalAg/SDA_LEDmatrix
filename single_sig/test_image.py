import requests
import pixoo_reset
from requests_toolbelt.multipart.encoder import MultipartEncoder


def main():
    pixoo_reset.reset_display()

    pixoo_url = 'http://iot.digitalag.kr:5000/image?host=pixoo2'

    with open('test.png', 'rb') as file:
        m = MultipartEncoder(
            fields={
                'image': ('test.png', file, 'image/png'),
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
