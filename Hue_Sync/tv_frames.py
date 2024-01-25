import asyncio
import websockets
import cv2
import numpy as np
import base64

# Set your LG TV IP address
tv_ip = "192.168.0.52"

async def capture_frames():
    uri = f"ws://{tv_ip}:3000"
    i = 0

    try:
        async with websockets.connect(uri) as websocket:
            print("Connected to the WebSocket")

            while True:
                # Send a request for a screenshot
                await websocket.send('{"type":"request","id":"' + str(i) + '","uri":"ssap://com.webos.service.tvaudio/turnOn"}')
                i += 1

                # Receive the screenshot data
                screenshot_data = await websocket.recv()
                screenshot_data = screenshot_data.strip()  # Strip leading and trailing whitespaces
                print("Received screenshot data")
                print("screenshot_data:", screenshot_data)

                try:
                    # Print the length of the received screenshot_data
                    print("Length of screenshot_data:", len(screenshot_data))

                    # Ensure the length is a multiple of 4 before decoding
                    padding = b'=' * (4 - len(screenshot_data) % 4)
                    padded_data = screenshot_data.encode('utf-8') + padding

                    # Use np.frombuffer directly on the base64-decoded bytes
                    screenshot_np = np.frombuffer(base64.b64decode(padded_data), dtype=np.uint8)

                    # Decode the NumPy array to an image
                    frame = cv2.imdecode(screenshot_np, cv2.IMREAD_COLOR)

                    # Check if the frame is valid before displaying
                    if frame is not None and frame.size != 0:
                        # Display the captured frame or process it as needed
                        cv2.imshow("Frame", frame)

                except base64.binascii.Error as e:
                    print(f"Error decoding base64: {e}")

                # Break the loop when 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"WebSocket connection closed with error: {e}")
    except asyncio.CancelledError:
        print("Task cancelled.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        # Close the WebSocket connection
        if websocket and websocket.open:
            await websocket.close()

        # Close the OpenCV window and cleanup
        cv2.destroyAllWindows()

# Run the event loop using asyncio.run()
asyncio.run(capture_frames())
