import tkinter as tk
from datetime import datetime, timezone, timedelta

def get_current_time(timezone_str):
    tz = timezone(timedelta(hours=timezone_str))
    current_time = datetime.now(tz).strftime("%H:%M:%S")
    return current_time

def update_time():
    current_time_icelandic = get_current_time(0)  # Iceland: UTC
    current_time_danish = get_current_time(2)     # Denmark: UTC+2
    
    clock_label_icelandic.config(text=f"Icelandic Time: {current_time_icelandic}")
    clock_label_danish.config(text=f"Danish Time: {current_time_danish}")
    
    root.after(1000, update_time)

# Create the main application window
root = tk.Tk()
root.title("Multi-Timezone Clock App")
root.geometry("400x200")  # Set the window size

# Create labels for Icelandic and Danish times with updated styling
clock_label_icelandic = tk.Label(root, font=("Helvetica", 18), fg="blue")
clock_label_icelandic.pack(pady=(20, 0))  # Add vertical padding

clock_label_danish = tk.Label(root, font=("Helvetica", 18), fg="green")
clock_label_danish.pack()

# Start the clock update loop
update_time()

# Run the Tkinter event loop
root.mainloop()
