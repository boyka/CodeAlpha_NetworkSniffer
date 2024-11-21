from scapy.all import sniff

# Function to process each packet
def packet_callback(packet):
    print(packet.summary())  # Print a summary of the packet

# Start sniffing packets
def start_sniffer(interface=None):
    print("Starting the sniffer...")
    # If an interface is specified, use it; otherwise, sniff all interfaces
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # Optionally specify the network interface (e.g., 'eth0', 'wlan0')
    start_sniffer(interface=None)  # Change to your specific interface if needed