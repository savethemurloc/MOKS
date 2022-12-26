from scapy.all import *


packets = rdpcap('/home/alexandr/dump.pcap')
print(len(packets))
# for packet in packets:
#     print(packet)
#     print(dir(packet))
#     print(packet.payload)
#     print(packet['TCP'])
#     print(packet['TCP'].flags)
#
