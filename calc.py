from logging import root
from tkinter import *
root=Tk()

root.geometry('600x400')
root.title('калькулятор300000')
oper_num = 1

global num_count
#с помощью команды global делаем переменную num_count видной для функций
#если global не написать - функции будут ругаться что num_count не существует
#строку global num_count надо писать каждый раз, перед тем как ты хочешь использовать переменную num_count
num_count = 0

#--------- область создания функций ------
#создай функцию school_hack(event), которая 10 раз выводит текст "готовится взлом школы"

def close_win(event):
  root.quit()
  print("программа закрылась с кодом ошибки 0")

def school_hack(event):
  print('готовится взлом школы')
  print('происходит взлом школы')
  print('школа взломана')

def bt1(Event):
  global num_count
  #вызываем глобальную переменную
  if num_count !=0:
  #проверяем счетчик (напоминаю: он меняется каждый раз когда мы нажимаем на знак операции). если счётчик был изменён хоть раз мы
    tablo[2]=1
  #меняем второй элемент табла
  else:
  #иначе (если счётчик так же равен 0, то есть операция не выбиралась) 
    tablo[0]=1
  #меняем нолевой элемент табла
  lbl1.configure(text=tablo)
  #обновляем табло каждый раз когда нажимаем на кнопки


def bt2(Event):
  global num_count
  if num_count !=0:
    tablo[2]=2
  else:
    tablo[0]=2
  lbl1.configure(text=tablo)
    
def bt3(Event):
  global num_count
  if num_count !=0:
    tablo[2]=3
  else:
    tablo[0]=3
  lbl1.configure(text=tablo)

def bt4(Event):
  global num_count
  if num_count !=0:
    tablo[2]=4
  else:
    tablo[0]=4
  lbl1.configure(text=tablo)

def bt5(Event):
  global num_count
  if num_count !=0:
    tablo[2]=5
  else:
    tablo[0]=5
  lbl1.configure(text=tablo)

def bt6(Event):
  global num_count
  if num_count !=0:
    tablo[2]=6
  else:
    tablo[0]=6
  lbl1.configure(text=tablo)

def bt7(Event):
  global num_count
  if num_count !=0:
    tablo[2]=7
  else:
    tablo[0]=7
  lbl1.configure(text=tablo)

def bt8(Event):
  global num_count
  if num_count !=0:
    tablo[2]=8
  else:
    tablo[0]=8
  lbl1.configure(text=tablo)

def bt9(Event):
  global num_count
  if num_count !=0:
    tablo[2]=9
  else:
    tablo[0]=9
  lbl1.configure(text=tablo)

def bt10(Event):
  global num_count
  if num_count !=0:
    tablo[2]=0
  else:
    tablo[0]=0
  lbl1.configure(text=tablo)

def oper1(Event):
  tablo[1] = "+"
  lbl1.configure(text=tablo)
  global oper_num
  oper_num = 1
  global num_count
  #указали в функции что используется ГЛОБАЛЬНАЯ переменная num_count
  num_count += 1

def oper2(Event):
  tablo[1] = "-"
  lbl1.configure(text=tablo)
  global oper_num
  oper_num = 2
  global num_count
  num_count += 1
  
def oper3(Event):
  tablo[1] = "*"
  lbl1.configure(text=tablo)
  global oper_num
  oper_num = 3
  global num_count
  num_count += 1

def oper4(Event):
  tablo[1] = "/"
  lbl1.configure(text=tablo)
  global oper_num
  oper_num = 4
  #в дальшейшем будем использовать как код операции, которую нужно выполнить программе
  global num_count
  num_count += 1
  #как только нажимается любая клавиша с операцией меняем счётчик на +1. в дальнейшем будем проверять этот счётчик когда нажимаются цифры (если он не равен 0, то операция была выбрана и следует цифру записывать в третий элемент табла)

def a1(Event):
  global oper_num
  if oper_num == 1:
    tablo[4] = tablo[0] + tablo[2]
  if oper_num==2:
    tablo[4] = tablo[0] - tablo[2]
  if oper_num == 3:
    tablo[4] = tablo[0] * tablo[2]
  if oper_num == 4:
    tablo[4] = tablo[0] / tablo[2]
  lbl1.configure(text=tablo)

def clear(event):
  global num_count
  num_count = 0
  tablo[0] = "1"
  tablo[1] = "+"
  tablo[2] = "1"
  tablo[4] = "2"
  lbl1.configure(text=tablo)

tablo = ["1", "+", "1", "=", "2"]


#--------- область создания кнопок -------
btn1=Button(root,text='1', width = 3, height = 3)
btn2=Button(root,text='2', width=3,height=3)
btn3=Button(root,text='3', width=3,height=3)
btn4=Button(root,text='4', width=3,height=3)
btn5=Button(root,text='5', width=3,height=3)
btn6=Button(root,text='6', width=3,height=3)
btn7=Button(root,text='7', width=3,height=3)
btn8=Button(root,text='8', width=3,height=3)
btn9=Button(root,text='9', width=3,height=3)
btn10=Button(root,text='0', width=3,height=3)
btn11=Button(root,text='+', width=3,height=3)
btn12=Button(root,text='-', width=3,height=3)
btn13=Button(root,text='*', width=3,height=3)
btn14=Button(root,text='/', width=3,height=3)
btn15=Button(root,text='close', width=3,height=3)
btn16=Button(root,text='=', width = 3, height = 3)
btn17=Button(root,text='CL', width = 3, height = 3)
lbl1 = Label(root, text=tablo, height=3, font = "Arial 14")

#--------- область привязки к сетке -------
lbl1.grid(column = 3, row = 1)
btn1.grid(column = 0, row = 1)
btn2.grid(column = 1, row = 1)
btn3.grid(column = 2, row = 1)
btn4.grid(column = 0, row = 2)
btn5.grid(column = 1, row = 2)
btn6.grid(column = 2, row = 2)
btn7.grid(column = 0, row = 3)
btn8.grid(column = 1, row = 3)
btn9.grid(column = 2, row = 3)
btn10.grid(column = 0, row = 4)
btn11.grid(column = 1, row = 4)
btn12.grid(column = 2, row = 4)
btn13.grid(column = 0, row = 5)
btn14.grid(column = 2, row = 5)
btn15.grid(column=3,row=6)
btn16.grid(column=2, row=6)
btn17.grid(column=0, row=6)

#--------- область присваивания функций -------
btn1.bind('<Button-1>', bt1)
btn2.bind('<Button-1>', bt2)
btn3.bind('<Button-1>', bt3)
btn4.bind('<Button-1>', bt4)
btn5.bind('<Button-1>', bt5)
btn6.bind('<Button-1>', bt6)
btn7.bind('<Button-1>', bt7)
btn8.bind('<Button-1>', bt8)
btn9.bind('<Button-1>', bt9)
btn10.bind('<Button-1>', bt10)
btn11.bind('<Button-1>', oper1)
btn12.bind('<Button-1>', oper2)
btn13.bind('<Button-1>', oper3)
btn14.bind('<Button-1>', oper4)
btn15.bind('<Button-1>', close_win)
btn16.bind('<Button-1>', a1)
btn17.bind('<Button-1>', clear)
