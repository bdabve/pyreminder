#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QDialog
import socket
from threading import Thread
# from socketserver import ThreadingMixIn
from headers.demoClient import *
tcpClientA = None


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.textEditMsg = self.ui.textEditMsg
        self.ui.pushButtonSend.clicked.connect(self.dispMessage)

        self.show()

    def dispMessage(self):
        text = self.ui.lineEditMsg.text()
        self.ui.textEditMsg.append("Client: {}".format(self.ui.lineEditMsg.text()))
        tcpClientA.send(text.encode())
        self.ui.lineEditMsg.clear()


class ClientThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        host = socket.gethostname()
        port = 2055
        BUFFER_SIZE = 1024
        global tcpClientA
        tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpClientA.connect((host, port))
        while True:
            data = tcpClientA.recv(BUFFER_SIZE)
            window.textEditMsg.append("Server: {}".format(data.decode("utf-8")))
            tcpClientA.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    clientThread = ClientThread(window)
    window.exec()
    clientThread.start()
    sys.exit(app.exec_())
