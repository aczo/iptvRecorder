import socket
import struct
import os
import channels

def listen_to_group(sck, grp_ip):
  req = struct.pack("4sl", socket.inet_aton(grp_ip), socket.INADDR_ANY)
  sck.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)

#get port from environment config
MCAST_PORT = int(os.environ.get('UDP_PORT'))

IP_RECVORIGDSTADDR = 20

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_IP, IP_RECVORIGDSTADDR, 1)
# on this port, receives ALL multicast groups
sock.bind(('', MCAST_PORT))

chlist = channels.get_channels('channels.csv')

for ip, name in chlist.items():
  listen_to_group(sock, ip)

max_ancillary_size=28 #sizeof(struct sockaddr_in6)
bufsize = 10240

while True:
  data, ancdata, flags, client = sock.recvmsg(bufsize, socket.CMSG_SPACE(max_ancillary_size))
  for cmsg_level, cmsg_type, cmsg_data in ancdata:
    # Handling IPv4
    if cmsg_level == socket.SOL_IP and cmsg_type == IP_RECVORIGDSTADDR:
      family, port = struct.unpack('=HH', cmsg_data[0:4])
      port = socket.htons(port)

      if family != socket.AF_INET:
        raise TypeError(f"Unsupported socket type '{family}'")

      ip = socket.inet_ntop(family, cmsg_data[4:8])
      destination = (ip, port)
      print(ip)
      quit()
