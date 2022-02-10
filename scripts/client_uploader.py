import requests

'''
The curl command looks like this:
curl -X 'POST' \
    'http://127.0.0.1/image' \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'image=@HopeSandoval3.jpg'; type=image/jpeg
'''

file_name: str = "hope.jpg"

headers = {
    'accept': 'application/json',
    'Content-Type': 'multipart/form-data',
}

file = {
    'image': (file_name, open(file_name, 'rb'), 'image/jpg')
}

response = requests.post('http://127.0.0.1:8000/image', files=file)
