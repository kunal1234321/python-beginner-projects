import requests

url = input("Enter website URL: ")

try:
    response = requests.get(url, timeout=10)

    print("Status code:", response.status_code)

    if response.status_code == 200:
        print("Website is working!")
    else:
        print("Website responded with an error.")

except requests.RequestException:
    print("Could not connect to the website.")