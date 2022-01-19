import requests

file_name: str = "esther.jpg"
headers = {
    'accept': 'application/json',
    'Content-Type': 'multipart/form-data',
}

files = {
    'image': ('IMG_0872.JPG;type', open('IMG_0872.JPG;type', 'rb')),
}
response = requests.post('http://127.0.0.1:8000/image', headers=headers, files=files)

# This method is wrong. The curl command was using a -F for form, you need to emulate the
# same method in Python.
