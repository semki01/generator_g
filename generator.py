from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
question = QLabel('В каком году канал получил "золотую кнопку" от Youtube?')
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
layout_main = QVBoxLayout
layout_main.addWidget(quetion, alignment = Qt.AlignCenter)


main_win.show()
app.exec_()