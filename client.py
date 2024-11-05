import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data_for_send="hello server"
sdata=data_for_send.encode("UTF-8")
sock.sendto(sdata,("127.0.0.1",50000))
rdata,address=sock.recvfrom(512)
data=rdata.decode("UTF-8")
print("data recived from {} : \n {} ".format(address,data))