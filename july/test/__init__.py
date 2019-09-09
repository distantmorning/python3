import os

os.makedirs('./image/', exist_ok=True)
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
IMAGE_URL = "https://s3.qingbuyaohaixiu.com/image/d13403581c70046c23f44429e2dea348.jpeg"


def urllib_download():
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './image/img1.png')


def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    with open('./image/img2.png', 'wb') as f:
        f.write(r.content)


def chunk_download():
    import requests
    r = requests.get(IMAGE_URL, stream=True)
    with open('./image/img3.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)


urllib_download()
print('download img1')
request_download()
print('download img2')
chunk_download()
print('download img3')