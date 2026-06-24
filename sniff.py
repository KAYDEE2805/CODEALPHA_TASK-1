from scapy.all import sniff, TCP, IP, UDP

def sniffed_packet(packet):
    print("\n ===== Packet sniffed =====")

    if packet.haslayer(IP):
        print("Source IP        :", packet[IP].src)
        print("Destination IP   :", packet[IP].dst)
        print("Protocol         :", packet[IP].proto)

    if packet.haslayer(TCP):
        print("TCP Port:", packet[TCP].sport, "->", packet[TCP].dport)

    if packet.haslayer(UDP):
        print("UDP Port:", packet[UDP].sport, "->", packet[UDP].dport)

    print(packet.summary())

print("sniffing")
sniff(prn=sniffed_packet)

print("\n captured")