import tkinter as tk
import ipaddress

def calculate_ip_info():
    ip_str = ip_entry.get()
    subnet_mask_str = subnet_mask_entry.get()
    
    try:
        ip = ipaddress.ip_address(ip_str)

        # Determine IP class
        if ip.version == 4:
            first_byte = int(ip.exploded.split(".")[0])
            if first_byte <= 127:
                ip_class = "A"
            elif first_byte <= 191:
                ip_class = "B"
            elif first_byte <= 223:
                ip_class = "C"
            elif first_byte <= 239:
                ip_class = "D (Multicast)"
            else:
                ip_class = "E (Reserved)"
        else:
            ip_class = "IPv6"

        network = ipaddress.ip_network(f"{ip}/{subnet_mask_str}", strict=False)
        network_address = network.network_address
        broadcast_address = network.broadcast_address

        # Calculate the number of hosts in the subnet
        num_hosts = len(list(network.hosts()))
        
        # Calculate the number of usable hosts
        usable_hosts = num_hosts - 2
        
        # Calculate the usable IP range
        usable_ip_range = f"{network_address + 1} to {broadcast_address - 1}"

        result_label.config(
            text=f"IP Address: {ip}\n"
                 f"IP Class: {ip_class}\n"
                 f"Network Address: {network_address}\n"
                 f"Subnet Mask: {network.prefixlen}\n"
                 f"Broadcast Address: {broadcast_address}\n"
                 f"Number of Hosts: {num_hosts}\n"
                 f"Number of Usable Hosts: {usable_hosts}\n"
                 f"IP Range: {network.network_address} to {broadcast_address}\n"
                 f"Usable IP Range: {usable_ip_range}\n"
                 f"Is Private IP: {ip.is_private}\n"
                 f"Is Global IP: {ip.is_global}\n"
                 f"IP Version: {'IPv4' if ip.version == 4 else 'IPv6'}"
        )

    except ValueError as e:
        result_label.config(text=f"Invalid IP Address or Subnet Mask: {e}")

# Create a tkinter window
window = tk.Tk()
window.title("IP Information Calculator")

# Create and configure input fields and labels
ip_label = tk.Label(window, text="Enter an IP Address:")
ip_label.pack()

ip_entry = tk.Entry(window)
ip_entry.pack()

subnet_mask_label = tk.Label(window, text="Enter a Subnet Mask in CIDR notation (e.g., /24):")
subnet_mask_label.pack()

subnet_mask_entry = tk.Entry(window)
subnet_mask_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_ip_info)
calculate_button.pack()

result_label = tk.Label(window, text="", justify=tk.LEFT)
result_label.pack()

# Start the tkinter main loop
window.mainloop()
