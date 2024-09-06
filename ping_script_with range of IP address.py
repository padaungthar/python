import os
import socket
import ipaddress
import subprocess

# Function to ping a device and check if it's online
def ping_device(ip):
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")  # Unix-based system
    # For Windows, replace with `ping -n 1 {ip}`
    return response == 0  # returns True if the device is online

# Function to get device info if online
def get_device_info_nmap(ip):
    try:
        # Run nmap to get details about the device
        nmap_scan = subprocess.run(["nmap", "-O", "--osscan-guess", ip], capture_output=True, text=True)
        scan_output = nmap_scan.stdout
        
        if "Running:" in scan_output:
            os_info = scan_output.split("Running:")[1].split("\n")[0].strip()
        else:
            os_info = "Unknown OS"
        
        if "OS CPE:" in scan_output:
            os_version = scan_output.split("OS CPE:")[1].split("\n")[0].strip()
        else:
            os_version = "Unknown Version"
        
        if "MAC Address:" in scan_output:
            mac_address = scan_output.split("MAC Address:")[1].split(" ")[0].strip()
            manufacturer = scan_output.split("MAC Address:")[1].split("(")[1].split(")")[0].strip()
        else:
            mac_address = "Unknown MAC"
            manufacturer = "Unknown Manufacturer"
        
        hostname = socket.getfqdn(ip)
        
        return {
            "Hostname": hostname,
            "OS": os_info,
            "OS Version": os_version,
            "MAC Address": mac_address,
            "Manufacturer": manufacturer
        }
    except Exception as e:
        print(f"Error retrieving device info for {ip}: {e}")
        return None

# Input the starting and ending IP address from the user
start_ip = input("Enter the starting IP address (e.g., 192.168.1.10): ")
end_ip = input("Enter the ending IP address (e.g., 192.168.1.20): ")

# Validate and generate the range of IP addresses
try:
    start_ip_obj = ipaddress.ip_address(start_ip)
    end_ip_obj = ipaddress.ip_address(end_ip)
    
    if start_ip_obj > end_ip_obj:
        print("Invalid range: Starting IP should be less than or equal to the ending IP.")
        exit()

except ValueError:
    print("Invalid IP address.")
    exit()

# Ping each device in the specified range and retrieve information if online
current_ip = start_ip_obj
while current_ip <= end_ip_obj:
    ip_str = str(current_ip)
    if ping_device(ip_str):
        print(f"Device {ip_str} is ONLINE.")
        device_info = get_device_info_nmap(ip_str)
        if device_info:
            print(f"Device Info: {device_info}")
    else:
        print(f"Device {ip_str} is OFFLINE.")
    
    current_ip += 1  # Move to the next IP in the range