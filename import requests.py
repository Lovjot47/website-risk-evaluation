import requests

def fetch_website(url):
    try:
        response = requests.get(url, timeout=10)
        return response.text
    except:
        return None