import pyshark

filename = "./mouse.pcapng"

cap = pyshark.FileCapture(filename, keep_packets=False)

