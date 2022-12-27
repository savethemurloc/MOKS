from scapy.all import *


packets = rdpcap('/home/alexandr/test_dump.pcap')
total_counter = len(packets)
dhcp_counter = 0
dns_counter = 0
arp_counter = 0
tcp_counter = 0
udp_counter = 0

for packet in packets:
    if (packet.haslayer(DHCP)):
        dhcp_counter = dhcp_counter + 1
    elif (packet.haslayer(DNS)):
        dns_counter = dns_counter + 1
    elif (packet.haslayer(ARP)):
        arp_counter = arp_counter + 1
    elif (packet.haslayer(TCP)):
        tcp_counter = tcp_counter + 1
    elif (packet.haslayer(UDP)):
        udp_counter = udp_counter + 1
other_counter = total_counter - arp_counter - dhcp_counter - dns_counter - tcp_counter - udp_counter

print(other_counter)