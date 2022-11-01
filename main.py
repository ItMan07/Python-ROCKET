from loader import *
from serial_port import *


# ======================================= ФУНКЦИИ ======================================================================


def turnLed():
    global flagBtnLed

    if flagBtnLed:
        flagBtnLed = False
        serialSend([0, 0])
    else:
        flagBtnLed = True
        serialSend([0, 1])


# ======================================= ИНТЕРФЕЙС ====================================================================


def load_UI():
    # ui.comPortsCB.addItems(portList)
    reloadComPortsCB()
    ui.reloadBtn.clicked.connect(reloadComPortsCB)
    serial.readyRead.connect(OnRead)
    ui.openBtn.clicked.connect(onOpen)
    ui.closeBtn.clicked.connect(OnClose)

    # ui.btnLed.clicked.connect(turnLed)

    ui.show()
    app.exec()


def main():
    load_UI()


if __name__ == "__main__":
    main()
