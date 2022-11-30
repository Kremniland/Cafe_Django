import requests

def test_api():
    result = requests.get('http://127.0.0.1:8000/viewset/coffe-api/')
    print(result.json())

test_api()