import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",50000))
rdata,address=s.recvfrom(1024)
data=rdata.decode("UTF-8")
data_for_send="hello client"
sdata=data_for_send.encode("UTF-8")
s.sendto(sdata,address)
print(data,address)