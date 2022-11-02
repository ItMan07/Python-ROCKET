from loader import *


def onOpen():
    serial.setPortName(ui.comPortsCB.currentText())
    serial.open(QIODevice.ReadWrite)


def OnClose():
    serial.close()
    ui.connectBtn.setText(strOFF)


def serialSend(data):
    txs = ""
    for val in data:
        txs += str(val) + ','
    txs = txs[:-1]
    txs += ';'
    serial.write(txs.encode())


def reloadComPortsCB():
    ui.comPortsCB.clear()
    ports = QSerialPortInfo().availablePorts()

    global portList
    portList = []
    for port in ports:
        portList.append(port.portName())
        # portList.append(port.systemLocation())
        # portList.append(port.description())

    ui.comPortsCB.addItems(portList)


def openSuccess():
    info = QMessageBox()
    info.setWindowTitle("Информация")
    info.setText("COM-порт был успешно открыт! \n")
    info.setInformativeText("Arduino устройство готово к работе")
    info.setIcon(QMessageBox.Information)
    info.setStandardButtons(QMessageBox.Ok)
    ui.connectBtn.setText(strON)
    info.exec_()
