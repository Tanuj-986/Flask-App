import requests

url = 'http://127.0.0.1:5000/upload'
files = {'file': open('D:\\Python\\response.wav', 'rb')}

response = requests.post(url, files=files)
print(response.text)
