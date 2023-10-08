from random import choice, shuffle
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QHBoxLayout, QMessageBox, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])

from card_window import *
from menu_window import *

class Question:
    current = None
    count_right = 0 #лічильник правильних відповідей
    count_ans = 0 #лічильник відповідей

    def __init__(self, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def got_right(self):
        Question.count_ans += 1
        Question.count_right += 1
        print(Question.count_ans)
        print(Question.count_right)

    def got_wrong(self):
        Question.count_ans += 1
        print(Question.count_ans)

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1,q2,q3,q4]
radio_buttons = [btn1, btn2, btn3, btn4]

main_win = QWidget()
main_win.setWindowTitle("Memory Card")
main_win.resize(600, 500)
main_win.move(200,200)
main_win.setLayout(main_line)

def new_question():
    Question.current = choice(questions) #вибираємо випадкове питання
    question.setText(Question.current.question)
    right_lb.setText(Question.current.right_answer)
    shuffle(radio_buttons)
    radio_buttons[0].setText(Question.current.right_answer)

    radio_buttons[1].setText(Question.current.wrong_answer1)
    radio_buttons[2].setText(Question.current.wrong_answer2)
    radio_buttons[3].setText(Question.current.wrong_answer3)


new_question()

def check_result():
    radio_group.setExclusive(False)
    # перевіряємо правильність відповіді
    if radio_buttons[0].isChecked():
        Question.current.got_right()
        result_lb.setText("Правильно")
        radio_buttons[0].setChecked(False)
    else:
        Question.current.got_wrong()
        result_lb.setText("Неправильно")

    radio_group.setExclusive(True)


def click_btn():
    if answer_btn.text() == "Відповісти":
        check_result()
        group_box.hide()
        answer_box.show()
        answer_btn.setText("Наступне питання")
    else:
        answer_box.hide()
        group_box.show()
        answer_btn.setText("Відповісти")
        new_question()


def relax():
    pause_time = int(time_box.value()) * 60
    main_win.hide()
    sleep(pause_time)
    main_win.show()


def menu_show():
    main_win.hide()
    count_ans_lb.setText(f"Кількість відповідей: {Question.count_ans}")
    count_right_lb.setText(f"Кількість правильних відповідей: {Question.count_right}")
    success_lb.setText(f"Успішність: {2/4*100}%")
    menu_win.show()

answer_btn.clicked.connect(click_btn)
sleep_btn.clicked.connect(relax)
menu_btn.clicked.connect(menu_show)

main_win.show()
app.exec_()

