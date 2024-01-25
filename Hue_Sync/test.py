import requests
from PIL import Image
from io import BytesIO

WEBOS_TV_IP = "192.168.0.52"  # Replace this with your WebOS TV's IP address
UMEDIA_API_PORT = 3000

def send_request(endpoint, payload=None):
    url = f"http://{WEBOS_TV_IP}:{UMEDIA_API_PORT}{endpoint}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error sending request to {url}: {e}")
        return None

def capture_screen(output_path):
    endpoint = "/screencapture"

    response = send_request(endpoint)
    print("Response:", response)  # Add this line for debugging
    
    if response is not None and response.get("returnValue", False):
        image_data = response.get("data", "")
        if image_data:
            # Convert image data to Pillow Image
            image = Image.open(BytesIO(image_data))
            
            # Save the captured screen to a file
            image.save(output_path)
            
            print(f"Screen captured and saved to {output_path}")
            return True
    else:
        print("Failed to capture screen.")
    
    return False

# Example: Capture the TV screen and save it to a file
output_path = 'C:\\Users\\willi\\Desktop\\media\\screenshot.jpg'  # Replace with your desired output path
capture_screen(output_path)
