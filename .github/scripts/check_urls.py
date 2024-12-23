import json
import requests

def check_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    with open('./templates.json', 'r') as file:
        data = json.load(file)
    
    for item in data:
        url = item.get('Url')
        if url and not check_url(url):
            print(f'URL check failed for {url}')
            exit(1) # Exit with error if any URL check fails

if __name__ == "__main__":
    main()