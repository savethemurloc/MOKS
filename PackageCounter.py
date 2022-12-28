from scapy.all import *


def countPackets(filepath):
    packets = rdpcap(filepath)
    total_counter = len(packets)
    dhcp_counter = 0
    dns_counter = 0
    arp_counter = 0
    tcp_counter = 0
    udp_counter = 0

    for pack in packets:
        if pack.haslayer(DHCP):
            dhcp_counter = dhcp_counter + 1
        elif pack.haslayer(DNS):
            dns_counter = dns_counter + 1
        elif pack.haslayer(ARP):
            arp_counter = arp_counter + 1
        elif pack.haslayer(TCP):
            tcp_counter = tcp_counter + 1
        elif pack.haslayer(UDP):
            udp_counter = udp_counter + 1

    other_counter = total_counter - arp_counter - dhcp_counter - dns_counter - tcp_counter - udp_counter

    return [arp_counter, dhcp_counter, dns_counter, tcp_counter, udp_counter, other_counter]

