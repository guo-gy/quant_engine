import requests
from bs4 import BeautifulSoup

def simple_spider(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else "No Title Found"
        return title
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    target = "https://example.com"
    result = simple_spider(target)
    print(f"Target: {target} | Title: {result}")
