import requests

# Replace with your Spotify client credentials
client_id = 'c4e3265a104343b7aa39f8228d4e76d2'
client_secret = 'f5bcd86b3ad14e77869856ce92228ab7'

# Set the headers
headers = {
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Length': '278',  # Update the content length as per your payload
    'Content-Type': 'application/json',
    'Host': 'clienttoken.spotify.com',
    'Origin': 'https://open.spotify.com',
    'Referer': 'https://open.spotify.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
}

# Set the data for the POST request
data = {
    'grant_type': 'client_credentials',
    # Add any other required parameters here
}

# Set the authentication
auth = (client_id, client_secret)

# Make the POST request
response = requests.post('https://accounts.spotify.com/api/token', headers=headers, json=data)

# Handle the response
if response.status_code == 200:
    # Process the response data here
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
