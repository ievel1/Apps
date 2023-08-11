import datetime
import pytz
import tkinter as tk
from tkinter import ttk

# Define color constants
BG_COLOR = "#E5E5E5"
LABEL_COLOR = "#333333"
TIME_COLOR = "#00AEEF"
HELVETICA_FONT = ("Helvetica", 25, "bold")
DIGITAL_7_FONT = ("digital-7", 35, "normal")  # Use the correct font name

def get_time_in_timezone(timezone):
    selected_timezone = pytz.timezone(timezone)
    current_time = datetime.datetime.now(selected_timezone)
    time_string = current_time.strftime("%H:%M:%S")
    return time_string

def update_time_labels():
    iceland_time = get_time_in_timezone('Atlantic/Reykjavik')
    denmark_time = get_time_in_timezone('Europe/Copenhagen')
    iceland_label.config(text=f"Iceland", font=HELVETICA_FONT, foreground=LABEL_COLOR)
    denmark_label.config(text=f"Denmark", font=HELVETICA_FONT, foreground=LABEL_COLOR)
    iceland_time_label.config(text=iceland_time, font=DIGITAL_7_FONT, foreground=TIME_COLOR)
    denmark_time_label.config(text=denmark_time, font=DIGITAL_7_FONT, foreground=TIME_COLOR)
    app.after(1000, update_time_labels)

app = tk.Tk()
app.title("Dual Time Clocks")

# Set the width and height for the initial window size
initial_width = 400
initial_height = 250

app.geometry(f"{initial_width}x{initial_height}")
app.configure(bg=BG_COLOR)

style = ttk.Style()
style.configure("TLabel", background=BG_COLOR)

frame = ttk.Frame(app)
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

denmark_label = ttk.Label(frame, wraplength=200, justify="center", font=HELVETICA_FONT, foreground=LABEL_COLOR)
denmark_label.grid(row=0, column=0, padx=20, pady=10)

iceland_label = ttk.Label(frame, wraplength=200, justify="center", font=HELVETICA_FONT, foreground=LABEL_COLOR)
iceland_label.grid(row=1, column=0, padx=20, pady=10)

denmark_time_label = ttk.Label(frame, wraplength=200, justify="center", font=DIGITAL_7_FONT, foreground=TIME_COLOR)
denmark_time_label.grid(row=0, column=1, padx=20, pady=10)

iceland_time_label = ttk.Label(frame, wraplength=200, justify="center", font=DIGITAL_7_FONT, foreground=TIME_COLOR)
iceland_time_label.grid(row=1, column=1, padx=20, pady=10)

# Force initial layout update
app.update()

update_time_labels()

app.mainloop()
