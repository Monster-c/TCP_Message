#-*- coding =utf-8 -*-
#@Time : 2020/11/27 21:58
#@Author : 曹显伟
#@File UDP_Client.py
#@Software: PyCharm

import socket
import threading

class TcpClient(object):

    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = addr

    def create_client(self):
        self.sock.connect(self.addr)
        print(self.sock.recv(1024).decode("UTF-8"))
        print("please enter message(enter 'exit' to quit the chat)")
        while True:
            message = input(">>>")
            if (message == "exit"):
                print('quit from the chatroom.....')
                break
            self.sock.send(message.encode("UTF-8"))
            print("response is>>>" + self.sock.recv(1024).decode("UTF-8"))

    def thread_run(self):
        lock = threading.Lock()
        try:
            lock.acquire()
            self.create_client()
        finally:
            lock.release()


if __name__ == '__main__':
    client = TcpClient(('127.0.0.1', 8089))
    client.create_client()

