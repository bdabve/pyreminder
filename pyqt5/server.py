#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 29.callServer.py
|      CREATED : 12-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : Server side application with PyQt5
|        USAGE : ./29.callServer.py
\ ====================================================================================================
"""

import sys
# from PyQt5 import QtGui
# from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog
# from PyQt5.QtCore import QCoreApplication
import socket
from threading import Thread
# from socketserver import ThreadingMixIn

conn = None
# from ui_files.server import *
from h_demoServer import *


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.textEditMsg = self.ui.textEditmessage
        self.ui.sendButton.clicked.connect(self.disp_msg)

        self.show()

    def disp_msg(self):
        global conn
        text = self.ui.lineEditmessage.text()
        conn.send(text.encode('utf-8'))
        self.textEditMsg.append('Server: {}'.format(self.ui.lineEditmessage.text()))
        self.ui.lineEditmessage.clear()


class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        TCP_IP = '127.0.0.1'
        TCP_PORT = 2055
        # BUFFER_SIZE = 1024
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT))
        threads = []
        tcpServer.listen(4)
        while True:
            global conn
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port, window)
            newthread.start()
            threads.append(newthread)
        for t in threads:
            t.join()


class ClientThread(Thread):
    def __init__(self, ip, port, window):
        Thread.__init__(self)
        self.window = window
        self.ip = ip
        self.port = port

    def run(self):
        while True:
            global conn
            data = conn.recv(1024)
            window.textEditMsg.append('Client: {}'.format(data.decode('utf-8')))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    serverThread = ServerThread(window)
    serverThread.start()
    window.exec()
    sys.exit(app.exec_())
