#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
            QApplication,QWidget,
            QHBoxLayout,QVBoxLayout,
            QGroupBox, QButtonGroup, QRadioButton,
            QPushButton, QLabel)
from random import shuffle, randint

class Question():
    def __init__(self,question , right_answer, wrong1, wrong2 , wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('сколько серий в ван пис','999' ,'987', '987', '1' ))
question_list.append(Question('кто живет на дне океана','звезда' ,'краб', 'мозги Армана', 'губка' ))
question_list.append(Question('кто твой тимейт','рак' ,'козел', 'петух', 'Арман' ))

app = QApplication([])

btn_OK = QPushButton('ответить')
lb_Question = QLabel('Сложный ответ')


RadioGroupBox = QGroupBox('Варианты ответа')


rbtn_1 = QRadioButton('вариант 1')
rbtn_2 = QRadioButton('вариант 2')
rbtn_3 = QRadioButton('вариант 3')
rbtn_4 = QRadioButton('вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QHBoxLayout()
Layout_ans3 = QHBoxLayout()
Layout_ans2.addWidget(rbtn_1)
Layout_ans2.addWidget(rbtn_2)
Layout_ans3.addWidget(rbtn_3)
Layout_ans3.addWidget(rbtn_4)



Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

RadioGroupBox.setLayout(Layout_ans1)

points = 0
AnsgroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('ПРАВ ТЫ ИЛИ НЕТ')
lb_Correct = QLabel('ОТВЕТ БУДЕТ ТУТ!')



layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsgroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsgroupBox)
AnsgroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)



def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide
    AnsgroupBox.show()
    btn_OK.setText('Следуйщий вопрос')

def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsgroupBox.hide()
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    question_list.remove(q)
    show_question()



def show_correct(res):
    '''показать результат - установим переданный текст в надпись "результат" и покажем нужную панель'''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответа'''
    global points
    if answers[0].isChecked():
        points += 1
        show_correct('Правельно! Your score.'+ str(points) + 'points')
    else:
        if answers[1].isChecked()or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно! Your score'+str(points) +'points')
      
def next_question():
    '''задает слудующий вопрос из списка'''
    window.cur_question = randint(0, len(question_list)-1)
    window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)

def click_Ok():
    if btn_OK.text() =='Ответить':
        check_answer()
    else:
        next_question()



window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo card')
window.cur_question = -1





btn_OK.clicked.connect(click_Ok)




next_question()
window.resize(400,300)
window.show()
app.exec()

