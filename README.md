# Net101
To test how TCP works:
1. In one terminal run:
  tshark -i lo -r TCP.pcap
2. In another terminal run:
  python3 testServerTCP.py
3. In another terminal run:
  python3 testClientTCP.py
  And send the messages you want to send (q to quit)
4. Go to tshark terminal and Ctrl-C

To test how UDP works:
1. In one terminal run:
  tshark -i lo -r UDP.pcap
2. In another terminal run:
  python3 testServerUDP.py
3. In another terminal run:
  python3 testClientUDP.py
  And send any message you want (q to quit, too)
4. Go to the tshark terinal and Ctrl-C

Open Wireshark and open either TCP.pcap or UDP.pcap. It is clearer if you sent the same messages on both TCP and UDP tests. You
can see how TCP established the connection via the three way handshake, and UDP didnt, and how TCP takes way more packets to send
the same messages.
