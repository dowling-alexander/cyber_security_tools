import requests

# URL of the API endpoint
url = 'https://crt.sh/?q=google.com&output=json'

# Sending the GET request
response = requests.get(url)

# Print the response content for debugging
#print("Response content:", response.text)

# Check if the response contains JSON data
if response.headers.get('Content-Type') == 'application/json':
    data = response.json()
    # Filtering and extracting the 'name_value' fields that contain 'dev'
    filtered_names = sorted(set(
        item['name_value'] for item in data if 'dev' in item['name_value']
    ))

    # Print the filtered and sorted list of names
    for name in filtered_names:
        print(name)
else:
    print("Error: The response is not in JSON format")
