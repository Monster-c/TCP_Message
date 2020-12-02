# -*- coding =utf-8 -*-
# @Time : 2020/11/28 17:04
# @Author : 曹显伟
# @File UDP_Client.py
# @Software: PyCharm

import socket
import threading


class UdpClient(object):

    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = addr

    def create_client(self):
        while True:
            msg = input('please enter what you want to send(enter "exit" to quit)>>>')
            if (msg == 'exit'):
                print('exit......')
                break
            self.sock.sendto(msg.encode('UTF-8'), self.addr)
            data, address = self.sock.recvfrom(1024)
            print('receive data from %s:%s' % self.addr + '\n'+ 'msg>>>' + data.decode('utf-8'))
        self.sock.close()


if __name__ == '__main__':
    server = UdpClient(('127.0.0.1', 8086))
    server.create_client()
