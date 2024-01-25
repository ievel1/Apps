import tkinter as tk
from tkinter import ttk, colorchooser
import requests
import json

# Replace with your actual bridge IP and username
bridge_ip = "192.168.0.227"
username = "xelG-6RyJVVOxY1G43Bq2YL4inh5HSHXEPsZDUR4"

def get_light_state(light_id):
    url = f"http://{bridge_ip}/api/{username}/lights/{light_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["state"]
    else:
        print(f"Failed to get state for light {light_id}. Status code: {response.status_code}")
        return {}

def control_lights(light_id, on, color=None, brightness=None):
    url = f"http://{bridge_ip}/api/{username}/lights/{light_id}/state"
    data = {"on": on}

    if color:
        data.update(color)

    if brightness is not None:
        data["bri"] = brightness

    response = requests.put(url, data=json.dumps(data))

    if response.status_code == 200:
        if "on" in data:
            print(f"Successfully turned {'on' if on else 'off'} light {light_id}")
        else:
            print(f"Successfully adjusted brightness of Light {light_id}")
    else:
        print(f"Failed to turn {'on' if on else 'off'} light {light_id}. Status code: {response.status_code}")

class HueControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hue Light Control")

        self.light_vars = {}
        self.create_widgets()
        self.update_light_states()

    def create_widgets(self):
        self.root.geometry("400x600")
        
        for light_id in range(1, 5):
            light_state = get_light_state(light_id)
            is_on = light_state.get("on", False)
            xy_color = light_state.get("xy", [0, 0])
            brightness = light_state.get("bri", 254)  # Default brightness if not available

            self.light_vars[light_id] = {
                "on": tk.BooleanVar(value=is_on),
                "color": self.xy_to_rgb(xy_color) if is_on else (255, 255, 255),
                "brightness": tk.DoubleVar(value=brightness),
            }

            # Light Frame
            light_frame = ttk.Frame(self.root, padding=(10, 10))
            light_frame.pack(pady=10)

            # Light Switch
            light_switch = ttk.Checkbutton(
                light_frame,
                text=f"Light {light_id}",
                variable=self.light_vars[light_id]["on"],
                command=lambda l=light_id: self.toggle_light(l),
            )
            light_switch.grid(row=0, column=0, columnspan=2)

            # Color Button
            color_button = ttk.Button(
                light_frame,
                text="Select Color",
                command=lambda l=light_id: self.choose_color(l),
            )
            color_button.grid(row=1, column=0, pady=5)

            # Color Preview
            color_preview = ttk.Label(
                light_frame,
                text="Color Preview",
                background="#FFFFFF",  # Default white
                width=10,
                relief="solid",
            )
            color_preview.grid(row=1, column=1, padx=5)

            # Brightness Slider
            brightness_slider = ttk.Scale(
                light_frame,
                from_=0,
                to=100,
                orient="horizontal",
                variable=self.light_vars[light_id]["brightness"],
                command=lambda val, l=light_id: self.adjust_brightness(l, val),  # Pass brightness value
            )
            brightness_slider.grid(row=2, column=0, columnspan=2, pady=5)

            # Save color_preview reference to dictionary
            self.light_vars[light_id]["color_preview"] = color_preview

    def toggle_light(self, light_id):
        light_var = self.light_vars[light_id]
        current_state = get_light_state(light_id)

        # Check if only brightness is being adjusted
        if light_var["on"].get() == current_state.get("on") and \
                light_var["color"] == self.xy_to_rgb(current_state.get("xy")) and \
                light_var["brightness"].get() != current_state.get("bri"):
            control_lights(light_id, light_var["on"].get(), {"bri": light_var["brightness"].get()})
        else:
            # If not, apply the regular toggle logic
            control_lights(light_id, light_var["on"].get(), {"xy": self.rgb_to_xy(light_var["color"])})

    def adjust_brightness(self, light_id, brightness_percent):
        brightness_value = int(float(brightness_percent) * 254 / 100)  # Convert percentage to brightness scale (0-254)

        # Check if the brightness is already set to the desired value
        current_brightness = get_light_state(light_id).get("bri")
        if brightness_value == current_brightness:
            return

        # If the light is off, set the brightness without turning it on
        if not self.light_vars[light_id]["on"].get():
            control_lights(light_id, False, {"bri": brightness_value})
        else:
            # Update the light brightness without changing the state
            control_lights(light_id, True, {"bri": brightness_value})
            
        print(f"Adjusted brightness of Light {light_id} to {brightness_percent}%")

    def choose_color(self, light_id):
        color = colorchooser.askcolor(initialcolor=self.light_vars[light_id]["color"])
        if color:
            self.light_vars[light_id]["color"] = tuple(int(c) for c in color[0])
            print(f"Selected color for Light {light_id}: {self.light_vars[light_id]['color']}")
            self.toggle_light(light_id)  # Turn on the light immediately with the new color
            self.update_color_preview(light_id)

    def update_light_states(self):
        for light_id in range(1, 5):
            light_state = get_light_state(light_id)
            is_on = light_state.get("on", False)
            xy_color = light_state.get("xy", [0, 0])
            brightness = light_state.get("bri", 254)

            self.light_vars[light_id]["on"].set(is_on)
            self.light_vars[light_id]["color"] = self.xy_to_rgb(xy_color) if is_on else (255, 255, 255)
            self.light_vars[light_id]["brightness"].set(brightness)
            self.update_color_preview(light_id)

    def update_color_preview(self, light_id):
        rgb_color = self.light_vars[light_id]["color"]
        hex_color = "#{:02x}{:02x}{:02x}".format(*rgb_color)
        self.light_vars[light_id]["color_preview"].config(background=hex_color)

    def xy_to_rgb(self, xy):
        x, y = xy
        # Convert XY color to RGB color (you can use your own conversion logic here)
        # This is a simple example, and you may need more advanced conversion
        r = int(x * 255)
        g = int(y * 255)
        b = 255 - r
        return r, g, b

    def rgb_to_xy(self, rgb):
        r, g, b = rgb
        r = r / 255.0
        g = g / 255.0
        b = b / 255.0

        # Apply gamma correction
        r = (r / 12.92) if (r <= 0.04045) else ((r + 0.055) / 1.055) ** 2.4
        g = (g / 12.92) if (g <= 0.04045) else ((g + 0.055) / 1.055) ** 2.4
        b = (b / 12.92) if (b <= 0.04045) else ((b + 0.055) / 1.055) ** 2.4

        # Wide RGB D65 conversion formula
        x = r * 0.664511 + g * 0.154324 + b * 0.162028
        y = r * 0.283881 + g * 0.668433 + b * 0.047685
        z = r * 0.000088 + g * 0.072310 + b * 0.986039

        xy_sum = x + y + z

        if xy_sum == 0:
            return [0, 0]

        x /= xy_sum
        y /= xy_sum

        return [x, y]

if __name__ == "__main__":
    root = tk.Tk()
    app = HueControlApp(root)
    root.mainloop()
