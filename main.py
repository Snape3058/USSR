#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

PORT = 23333
BUFSIZE = 1024

cli = False
try:
    import sys
    import thread
    import socket
    import time
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

    import mainForm
except Exception as importException:
    print importException
    cli = True


class cliForm:
    host = "127.0.0.1"

    def __init__(self):
        thread.start_new_thread(self.receive, ())

    def send(self):
        instr = raw_input("[" + self.host + "] ").split(':$:')
        if 2 == len(instr):
            self.host = instr[0]
            data = instr[1]
        else:
            data = instr[0]
        try:
            udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udpsocket.sendto(data, (self.host, PORT))
            udpsocket.close()
        except Exception as e:
            print e
        print "<<< send to " + self.host + " :\n    " + data + "\n"

    def receive(self):
        udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpsocket.bind(('', PORT))
        while True:
            try:
                data, host = udpsocket.recvfrom(BUFSIZE)
            except Exception as e:
                print e
            print "\n>>> received from " + host[0] + " :\n    " + data + "\n"

if cli and __name__ == '__main__':
    form_mainForm = cliForm()
    while True:
        form_mainForm.send()


class FmainForm(QMainWindow, mainForm.Ui_Sender):
    usingflag = False

    def __init__(self, parent=None):
        super(FmainForm, self).__init__(parent)
        self.setupUi(self)
        self.textEdit_send.setFocus()
        self.connect(self.pushButton_sendmsg, SIGNAL(QString.fromUtf8("released()")), self.send)

    def send(self):
        udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = str(self.textEdit_send.toPlainText())
        host = str(self.lineEdit.text())
        while self.usingflag:
            pass
        self.usingflag = True
        try:
            udpsocket.sendto(data, (host, PORT))
            udpsocket.close()
            print "<<< " + str((data, (host, PORT)))
            self.textEdit_history.append("<<< send to " + host + " :\n    " + data)
            self.textEdit_history.append("")
        except Exception as e:
            print e
        finally:
            self.usingflag = False
        time.sleep(0.1)

    def receiveThread(self):
        self.textEdit_history.append(" ")
        udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udpsocket.bind(('', PORT))
        while True:
            try:
                data, host = udpsocket.recvfrom(BUFSIZE)
            except Exception as e:
                print e
            print ">>> " + str((data, host))
            while self.usingflag:
                pass
            self.usingflag = True
            self.textEdit_history.append(">>> received from " + host[0] + " :\n    " + data)
            self.textEdit_history.append("")
            self.usingflag = False
        udpsocket.close()


if not cli and __name__ == '__main__':
    app = QApplication(sys.argv)
    form_mainForm = FmainForm()
    form_mainForm.show()
    thread.start_new_thread(form_mainForm.receiveThread, ())
    app.exec_()
