import ipaddress

def calculate_subnet_info(ip_with_subnet):
    # Create an IP network object from the provided IP and subnet
    network = ipaddress.IPv4Network(ip_with_subnet, strict=False)
    
    # Calculate the network address
    network_address = network.network_address
    
    # Calculate the broadcast address
    broadcast_address = network.broadcast_address
    
    # Calculate the usable IP range
    usable_ips = list(network.hosts())
    
    # Determine the IP class
    first_octet = int(str(network.network_address).split('.')[0])
    
    if first_octet >= 1 and first_octet <= 126:
        ip_class = 'Class A'
    elif first_octet >= 128 and first_octet <= 191:
        ip_class = 'Class B'
    elif first_octet >= 192 and first_octet <= 223:
        ip_class = 'Class C'
    elif first_octet >= 224 and first_octet <= 239:
        ip_class = 'Class D (Multicast)'
    elif first_octet >= 240 and first_octet <= 255:
        ip_class = 'Class E (Experimental)'
    else:
        ip_class = 'Unknown Class'

    # Output results
    print(f"IP Address with Subnet: {ip_with_subnet}")
    print(f"Network Address: {network_address}")
    print(f"Broadcast Address: {broadcast_address}")
    print(f"Usable IP Range: {usable_ips[0]} - {usable_ips[-1]}")
    print(f"Total Usable IPs: {len(usable_ips)}")
    print(f"IP Class: {ip_class}")

# Main execution
if __name__ == "__main__":
    # User input for the IP address with subnet (CIDR notation)
    ip_with_subnet = input("Enter an IP address with subnet (e.g., 8.8.0.0/22): ")
    
    # Calculate and display subnet information
    calculate_subnet_info(ip_with_subnet)
