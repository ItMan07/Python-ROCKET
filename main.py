from loader import *
from serial_port import *


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
        print(data[1])

    if data[0] == '1':
        print(f'Температура: {data[1]}')
        # ui.progBarTemp.setValue(data[1])
        ui.progBarTemp.setValue(0)
        ui.lcdTemp.display(4.5)

    if data[0] == '2':
        print(f'Давление: {data[1]}')
        # ui.progBarPressure.setValue(data[1])
        ui.progBarPressure.setValue(0)
        ui.lcdPressure.display(4.5)

    if data[0] == '3':
        print(f'Высота: {data[1]}')
        # ui.progBarAltitude.setValue(data[1])
        ui.progBarAltitude.setValue(0)
        ui.lcdAltitude.display(4.5)

    if data[0] == '4':
        print(f'Угол сервопривода: {data[1]}')
        ui.progBarServo.setValue(data[1])
        ui.progBarServo.setValue(0)

    if data[0] == '5':
        print(f'Состояние парашюта: {data[1]}')

    if data[0] == '6':
        print(f'Скорость: {data[1]}')
        ui.lcdSpeed.display(4.5)

    if data[0] == '7':
        print(f'Ускорение: {data[1]}')
        ui.lcdAcceleration.display(4.5)

    else:
        print(data[0])


# ======================================= ФУНКЦИИ ======================================================================

def sendServoValue():
    val = ui.dialServo.value()
    ui.progBarServo.setValue(val)
    print(f"Значение крутилки сервопривода: {val}")


def setBtnParachute():
    if ui.sliderParachute.value() == 2:
        ui.btnParachute.setEnabled(True)
    else:
        ui.btnParachute.setDisabled(True)


# ======================================= ИНТЕРФЕЙС ====================================================================


def load_UI():
    # ui.comPortsCB.addItems(portList)
    reloadComPortsCB()
    ui.reloadBtn.clicked.connect(reloadComPortsCB)
    serial.readyRead.connect(OnRead)

    ui.openBtn.clicked.connect(onOpen)
    ui.closeBtn.clicked.connect(OnClose)

    ui.lcdTemp.setDecMode()
    ui.lcdAltitude.setDecMode()
    ui.lcdSpeed.setDecMode()
    ui.lcdPressure.setDecMode()
    ui.lcdAcceleration.setDecMode()

    ui.btnServo.clicked.connect(sendServoValue)

    ui.sliderParachute.valueChanged.connect(setBtnParachute)

    ui.show()
    app.exec()


if __name__ == "__main__":
    load_UI()
