import json
import requests

def check_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        # Consider checking for other successful status codes if relevant
        return response.status_code == 200
    except requests.RequestException:
        return False

def main():
    with open('./templates.json', 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            exit(1)
    
    # Access the 'Templates' key in the root object
    if 'Templates' in data:
        templates = data['Templates']
    else:
        print("JSON does not contain 'Templates'")
        exit(1)

    if not isinstance(templates, list):
        print("'Templates' is not a list")
        exit(1)

    for item in templates:
        # Ensure each item is a dictionary and has a 'Url' key
        if isinstance(item, dict) and 'Url' in item:
            url = item['Url']
            if not check_url(url):
                print(f'URL check failed for {url}')
                exit(1) # Exit with error if any URL check fails
        else:
            print(f"Item is not a dictionary or missing 'Url' key: {item}")
            exit(1)

if __name__ == "__main__":
    main()