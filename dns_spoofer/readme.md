<h3>Steps:</h3>
1. pip install netfilterqueue <br>
2. pip install scapy <br>
3. iptables -I FORWARD -j NFQUEUE --queue-num 0      (forward/output/input)
4. Head to the directory that contain arp_spoof file <br>
5. run command (e.g: python arp_spoof.py ) <br>
6. Head to the directory that contain dns_spoof file <br>
7. Open terminal <br>
8. run command (e.g: python dns_spoofer.py ) <br>
<br>
Use --help for help or view other option
