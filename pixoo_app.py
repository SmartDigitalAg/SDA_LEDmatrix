import streamlit as st
import requests
from single_sig import pixoo_reset
from requests_toolbelt.multipart.encoder import MultipartEncoder
import io


def format_text(text):
    """5글자마다 줄바꿈을 추가하는 함수"""
    formatted = ''
    for i in range(0, len(text), 5):
        chunk = text[i:i + 5]
        formatted += chunk + '\n'
    return formatted.strip()


def send_text_to_pixoo(host, text):
    """Send text to Pixoo display"""
    pixoo_url = f'http://iot.digitalag.kr:5000/text?host={host}'

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'text': format_text(text),
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

    try:
        response = requests.post(pixoo_url, headers=headers, data=data)
        if response.status_code == 200:
            st.success(f'Successfully sent text to {host}')
        else:
            st.error(f'Error sending text to {host}: {response.status_code} - {response.text}')
    except Exception as e:
        st.error(f'Error connecting to {host}: {str(e)}')


def send_image_to_pixoo(host, image_file):
    """Send image to Pixoo display"""
    pixoo_url = f'http://iot.digitalag.kr:5000/image?host={host}'

    try:
        # Create MultipartEncoder
        m = MultipartEncoder(
            fields={
                'image': (image_file.name, image_file, 'image/png'),
                'x': '0',
                'y': '0',
                'push_immediately': 'true'
            }
        )

        # Send request
        response = requests.post(
            pixoo_url,
            data=m,
            headers={'Content-Type': m.content_type}
        )

        if response.status_code == 200:
            st.success(f'Successfully sent image to {host}')
        else:
            st.error(f'Error sending image to {host}: {response.status_code} - {response.text}')
    except Exception as e:
        st.error(f'Error sending image to {host}: {str(e)}')


def main():
    st.title('Pixoo64 컨트롤러')

    # Reset button
    if st.button('화면 초기화'):
        try:
            pixoo_reset.reset_display()
            st.success('pixoo 선택')
        except Exception as e:
            st.error(f'Error resetting display: {str(e)}')

    # Host selection
    host = st.selectbox('pixoo 선택 (1: 문앞, 2: 연구실 중앙)',
                        options=['pixoo1', 'pixoo2', 'all'])

    # Mode selection
    mode = st.radio("유형 선택", ["Text", "Image"])

    if mode == "Text":
        # Text input with character limit
        text = st.text_area('Enter Message (max 15 characters)',
                            height=100,
                            max_chars=15)

        # Preview formatted text
        if text:
            st.write('Preview (5글자마다 줄바꿈):')
            st.text(format_text(text))

        # Send text button
        if st.button('메시지 입력'):
            if not text:
                st.warning('메세지 입력해 주세요')
                return
            if len(text) > 15:
                st.error('15자 이내로 작성')
                return

            send_text_to_pixoo(host=host, text=text)

    else:  # Image mode
        # Image upload
        uploaded_file = st.file_uploader("이미지 선택", type=['png', 'jpg', 'jpeg'])

        if uploaded_file is not None:
            # Display preview
            st.image(uploaded_file, caption='Preview', use_column_width=True)

            # Send image button
            if st.button('이미지 전송'):
                send_image_to_pixoo(host=host, image_file=uploaded_file)


if __name__ == '__main__':
    main()