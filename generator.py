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
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(guestion, aligment = Qt.Aligncenter)
layoutH2.addWidget(btn_answer1, aligment = Qt.Aligncenter)
layoutH3.addWidget(btn_answer2, aligment = Qt.Aligncenter)
layoutH2.addWidget(btn_answer3, aligment = Qt.Aligncenter)
layoutH3.addWidget(btn_answer4, aligment = Qt.Aligncenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)



def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Верно!\nВы выиграли гироскутер')
    victory_win.exec_()

def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Нет в 2015 году\n Не повезло не фортануло')
main_win.show()
app.exec_()
