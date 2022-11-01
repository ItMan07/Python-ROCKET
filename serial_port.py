from loader import *

def OnRead():
    # if not serial.canReadLine(): return  # выходим если нечего читать
    rx = serial.readLine()
    rx = str(rx, 'utf-8').strip()
    data = re.split("[,;]", rx)

    # data = rx
    print(data)

    if data[0] == '100':  # ПОДКЛЮЧЕНИЕ
        if data[1] == '1':
            openSuccess()
            print("Модуль Arduino подключен")
        if data[1] == '2':
            print("Модули подключены")
        if data[1] == '3':
            print("Модуль NRF24L01 подключен")

    if data[0] == '0':
        if data[1] == '0':
            pass
        elif data[1] == '1':
            pass

    if data[0] == '1':
        print(f'Температура: {data[1]}')

    if data[0] == '2':
        print(f'Давление: {data[1]}')

    if data[0] == '3':
        print(f'Высота: {data[1]}')

    if data[0] == '4':
        print(f'Угол сервопривода: {data[1]}')

    if data[0] == '5':
        print(f'Состояние парашюта: {data[1]}')

    if data[0] == '6':
        print(f'Скорость: {data[1]}')

    if data[0] == '7':
        print(f'Ускорение: {data[1]}')


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

