from PyQt5.QtWidgets import QApplication
from time import sleep
app = QApplication([])

from random import choice, shuffle

from memo___card_layout import *
from memo___app import *

list_rb = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

#меню 
def menu_generation():
    if cur_q.attempts != 0:
        result = (cur_q.correct/cur_q.attempts) * 100
    else:
        result = 0

    text = f'Разів відповіли {cur_q.attempts}\n'\
           f'Вірних відповідей {cur_q.correct}\n'\
           f'Успішність {round(result, 2)} %'
    
    lb_statistic.setText(text)
    window_card.hide()
    menu_win.show()


print("hello \nworld!")

def back_to_menu():
    menu_win.hide()
    window_card.show()


class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question # вопрос
        self.answer = answer # правильну відповідь
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2  
        self.wrong_answer3 = wrong_answer3 
        self.correct = 0
        self.attempts = 0

    def got_right_new(self):
        self.correct += 1
        self.attempts += 1
        

    def got_wrong(self):
        self.attempts += 1
       

def rest():
    window_card.hide()
    n = sp_rest.value()
    sleep(n)
    window_card.show()

def switch_screen():
    if btn_next.text() == "Відповісти":
        RadioGroupBox.hide()
        AnsGroupBox.show()
        check_result()
        btn_next.setText("Наступне питання")
    else:
        RadioGroupBox.show()
        AnsGroupBox.hide()
        new_question()
        btn_next.setText("Відповісти")

def new_question():
   
    global cur_q
    cur_q = choice(list_questions)
    lb_Correct.setText(cur_q.answer)
    lb_Question.setText(cur_q.question)

    shuffle(list_rb)

    list_rb[0].setText(cur_q.wrong_answer1) 
    list_rb[1].setText(cur_q.wrong_answer2)
    list_rb[2].setText(cur_q.wrong_answer3)
    list_rb[3].setText(cur_q.answer)

    shuffle(list_rb)


def check_result():
    for radio_button in list_rb:
        if radio_button.isChecked():
            if radio_button.text() == lb_Correct.text():
                lb_Result.setText("Правильно!")
                cur_q.got_right_new()
                radio_button.setChecked(False)
            else:
                lb_Result.setText("Не правильно!")
                cur_q.got_wrong()
                radio_button.setChecked(False)


def clear():
    le_question.clear()
    le_wrong_ans2.clear()
    le_wrong_ans1.clear()
    le_wrong_ans3.clear()
    le_right_ans.clear()

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                    le_wrong_ans1.text(), le_wrong_ans2.text(), le_wrong_ans3.text() )
    list_questions.append(new_q)
    clear()

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')





list_questions = [q1, q2, q3, q4]


new_question()
btn_clear.clicked.connect(clear)
btn_rest.clicked.connect(rest)
btn_next.clicked.connect(switch_screen)
btn_menu.clicked.connect(menu_generation)
btn_back.clicked.connect(back_to_menu)
btn_add_question.clicked.connect(add_question)
#menu_win.show()
app.exec_()