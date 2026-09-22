import requests

urls = [
    "https://example.com",
    "https://github.com",
    "https://google.com"
]

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        print(url, "-", response.status_code)

    except requests.RequestException:
        print(url, "- Connection failed")