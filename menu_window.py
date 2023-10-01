from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QRadioButton, QHBoxLayout, QMessageBox, QWidget, QPushButton, QLabel, QVBoxLayout, QSpinBox, QGroupBox, QButtonGroup

menu_win = QWidget()
menu_win.setWindowTitle("Memory Card Menu")
menu_win.resize(400, 200)
menu_win.move(200,200)

stat_lb = QLabel("Статистика:")
stat_lb.setStyleSheet('font-size: 19px; font-weight: bold;')

count_ans_lb = QLabel("Кількість відповідей: 0")
count_right_lb = QLabel("Кількість правильних відповідей: 0")
success_lb = QLabel("Успішність: 0%")

vline = QVBoxLayout()
vline.addWidget(stat_lb)
vline.addWidget(count_ans_lb)
vline.addWidget(count_right_lb)
vline.addWidget(success_lb)

menu_win.setLayout(vline)
