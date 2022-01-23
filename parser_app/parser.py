import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://rezka.ag"
URL = "https://rezka.ag/latest/1"

HEADERS = {
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

@csrf_exempt
def get_html(url, params=''):
    req =requests.get(url, headers=HEADERS, params=params)
    return req

@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    cartoon = []

    for item in items:
        cartoon.append(
            {
                'title': item.find('div', class_='b-content__inline_item-link').get_text(),
                'image': HOST + item.find('div', class_="b-content__inline_item-cover").find('img').get('src')
            }
        )
        return cartoon

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.static_code == 200:
        cartoon = []
        for page in range(0,1):
            html = get_html(URL, params={'page': page})
            cartoon.extend(get_data(html.text))
            return cartoon

    else:
        raise ValueError('Error in parser function')
