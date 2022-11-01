# ======================================= ИМПОРТ БИБЛИОТЕК =============================================================

import re

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QIODevice
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtWidgets import QMessageBox

# from serialPort import OnRead, reloadComPortsCB

# ======================================= НАСТРОЙКИ ====================================================================


app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("Arduino UI")

flagBtnLed = False

serial = QSerialPort()
serial.setBaudRate(9600)
portList = []

strON = "🟢 Включено"
strOFF = "🔴 Выключено"
stop = False
