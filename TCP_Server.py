#-*- coding =utf-8 -*-
#@Time : 2020/11/27 21:51
#@Author : 曹显伟
#@File UDP_Server.py
#@Software: PyCharm

import socket
import threading
import time

class TcpServer(object):
    #处理链接
    def tcplink(self, sock, addr):
        # addr为tuple，内容为（ip地址，端口号）
        print('Accept new connection from %s:%s...' % addr)
        sock.send("Welcome to chatroom!".encode("UTF-8"))
        while True:
            #防止远程连接中断
            try:
                data = sock.recv(1024)
                print("from "+"%s:%s" % addr+">>>"+ data.decode("UTF-8"))
                time.sleep(1)
                if not data or data.decode('UTF-8') == 'exit':
                    print('Server close......')
                    break
                resp = input("please enter response message>>>")
                sock.send(resp.encode("UTF-8"))
            except ConnectionResetError as cre:
                print('error', cre)
                break
        sock.close()
        print('Connection from %s:%s closed.' % addr)

    def create_sokcet(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 监听端口
        s.bind(("127.0.0.1", 8089))
        s.listen(2)
        print("Waiting for connection...")
        #监听连接
        while True:
            # 接收一个新链接
            sock, addr = s.accept()
            print("seccessful connect!")
            # 创建新线程来处理TCP连接
            t = threading.Thread(target=self.tcplink, args=(sock, addr))
            t.start()


if __name__ == '__main__':
    server = TcpServer()
    server.create_sokcet()





