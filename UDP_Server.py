#-*- coding =utf-8 -*-
#@Time : 2020/11/28 16:57
#@Author : 曹显伟
#@File UDP_Server.py.py
#@Software: PyCharm

import socket
import threading
import time


class UdpServer(object):

    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = addr


    def create_server(self):
        #绑定端口
        self.sock.bind(self.addr)
        print('Seccessful create UDP Connection......')
        while True:
            data, address = self.sock.recvfrom(1024)
            print('receive data from %s:%s' % address + '\n' + 'msg>>>' + data.decode('UTF-8'))
            msg = input('please enter what you want to send>>>')
            if msg == 'close':
                print('Server close......')
                break
            self.sock.sendto(msg.encode('UTF-8'), address)

if __name__ == '__main__':
    server = UdpServer(('127.0.0.1', 8086))
    server.create_server()









# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(('127.0.0.1', 8086))
# print('Waiting for Connection......')
# #创建新进程（线程）
# def udp_link(sock,data,addr):
#     while True:
#         print('Received from %s:%s>>>' % addr, data.decode('utf-8'))
#         time.sleep(1)
#         if not data or data.decode('utf-8')=='exit':
#             break
#         msg = input('please enter message>>>')
#         sock.sendto(msg.encode('utf-8'), addr)
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
#
# def	receive_data(sock):
#     while True:
#         # 接收数据:
#         try:#
#             data, addr = sock.recvfrom(1024)
#             t=threading.Thread(target=udp_link,args=(sock,data,addr))
#             t.start()
#         except Exception as e: #[WinError 10054] 远程主机强迫关闭了一个现有的连接。
#             print('Connect close......')
#             pass #不处理此错误
# if __name__ == '__main__':
#     receive_data(s)





# def udp_link(self, sock, addr):
#     # addr为tuple，内容为（ip地址，端口号）
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send("Welcome to chatroom!".encode("UTF-8"))
#     while True:
#         # 防止远程连接中断
#         try:
#             data = sock.recv(1024)
#             print("from " + "%s:%s" % addr + ">>>" + data.decode("UTF-8"))
#             time.sleep(1)
#             if not data or data.decode('UTF-8') == 'exit':
#                 break
#             resp = input("please enter response message>>>")
#             sock.send(resp.encode("UTF-8"))
#         except ConnectionResetError as cre:
#             print('error', cre)
#             break
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)
#
#
# def create_socket(self, address):
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.bind(('127.0.0.1', 8089))
#     print('Waiting for connection......')
#     while True:
#         data, addr = s.recvfrom(1024)
#         print('Receive form %s:%s' % addr + '>>>'+data.decode('utf-8'))


