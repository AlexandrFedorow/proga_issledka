from tkinter import *
import creations_objects as create_object
import functions as function
import config


root = Tk()
root.title("graf")
root.geometry("1020x1020")
root.configure(bg='#c5c5c5')

scale = StringVar()#хранит текущий масштаб (размер)
ismasche = IntVar()#показывает есть ли сетка
iscorner = IntVar()#показывает есть ли углы
isline = IntVar()  #показывает есть ли линии

isline.set(0)
iscorner.set(0)
ismasche.set(1)
scale.set(1)

pol1 = Canvas(root, width=200, height=622, bg='#7a7a7a', highlightthickness=0)#окно слева
pol2 = Canvas(root, width=820, height=622, bg='#000', highlightthickness=0)    #окно с решеткой
pol3 = Canvas(root, width=1025, height=318, bg='#7a7a7a', highlightthickness=0) #окно снизу

btn1 = Button(root, width=8, text="Increase", fg="#000", command=function.increase)  #кнопка +
btn2 = Button(root, width=8, text="Reduce", fg="#000", command=function.reducee)    #кнопка -
btn3 = Button(root, width=8, text="Move left", fg="#000", command=function.left) #кнопка <-
btn4 = Button(root, width=8, text="Move right", fg="#000", command=function.right)#кнопка ->
btn5 = Button(root, width=8, text="Move up", fg="#000", command=function.upper)   #кнопка ^
btn6 = Button(root, width=8, text="Move down", fg="#000", command=function.down) #кнопка \/
btn7 = Button(root, text="Apply", fg="#000", command=function.apply)     #кнопка =
btn8 = Button(root, text="Help", fg="#000", command=function.help)      #кнопка ?

zagl1 = Label(root, text='Actions', bg='#7a7a7a') #заголовок 'действия'
zagl2 = Label(root, text='Settings', bg='#7a7a7a')#заголовок 'настройки'
zagl3 = Label(root, text='Scale', bg='#7a7a7a')   #подписть 'масштаб'
zagl4 = Label(root, text='Masche', bg='#7a7a7a')  #подпись 'сетка'
zagl6 = Label(root, text='Сorners', bg='#7a7a7a')  #подпись 'углы'(выделение углов)
zagl7 = Label(root, text='Line', bg='#7a7a7a')    #подписть 'линии'
zagl5 = Label(root, width=89, height=6, anchor='nw', text='[OK] The program started without errors', bg='#fff')

scale_entry = Entry(width=10, textvariable=scale)

ismasche_checkbutton = Checkbutton(text='on/off', bg='#7a7a7a', variable=ismasche)
iscorner_checkbutton = Checkbutton(text='on/off', bg='#7a7a7a', variable=iscorner)
isline_checkbutton = Checkbutton(text='on/off', bg='#7a7a7a', variable=isline)

#добавояем первому (левому) полю виджеты
canvas_widget1 = pol1.create_window(100, 20, window=btn1)
canvas_widget2 = pol1.create_window(100, 20, window=btn2)
canvas_widget3 = pol1.create_window(100, 20, window=btn3)
canvas_widget4 = pol1.create_window(100, 20, window=btn4)
canvas_widget5 = pol1.create_window(100, 20, window=btn5)
canvas_widget6 = pol1.create_window(100, 20, window=btn6)
canvas_widget7 = pol1.create_window(100, 20, window=btn7)
canvas_widget8 = pol3.create_window(100, 20, window=btn8)

canvas_text_widget1 = pol1.create_window(100, 20, window=zagl1)
canvas_text_widget2 = pol1.create_window(100, 20, window=zagl2)
canvas_text_widget3 = pol1.create_window(100, 20, window=zagl3)
canvas_text_widget4 = pol1.create_window(100, 20, window=zagl4)
canvas_text_widget5 = pol3.create_window(100, 20, window=zagl5)

canvas_entry_widget1 = pol1.create_window(100, 20, window=scale_entry)

canvas_check_widget1 = pol1.create_window(100, 20, window=ismasche_checkbutton)

pol1.create_rectangle(1, 160, 180, 340)# обводка настроек

main_menu = Menu()
file_menu = Menu()

file_menu.add_command(label="Save as", command=function.save) #command = Save_as)
file_menu.add_command(label="Open", command=function.open_schema)#command = Open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

main_menu.add_cascade(label="File", menu=file_menu)


root.config(menu=main_menu)

pol1.place(x=5, y=0)
pol2.place(x=210, y=0)
pol3.place(x=5, y=627)

btn1.place(x=10, y=35)
btn2.place(x=90, y=35)
btn3.place(x=10, y=70)
btn4.place(x=90, y=70)
btn5.place(x=10, y=105)
btn6.place(x=90, y=105)
btn7.place(x=75, y=300)
btn8.place(x=10, y=635)

zagl2.place(x=75, y=135)
zagl3.place(x=10, y=172)
zagl4.place(x=10, y=205)
zagl5.place(x=210, y=640)
zagl6.place(x=10, y=235)
zagl7.place(x=10, y=265)

scale_entry.place(x=70, y=170)

ismasche_checkbutton.place(x=70, y=205)
iscorner_checkbutton.place(x=70, y=235)
isline_checkbutton.place(x=70, y=265)

create_object.Masche(pol2, config.MASCHE_SCALE, config.MASCHE_MODE)#создание сетки

config.SCALE = scale      #кидаем масштаб в конф
config.ISMASCHE = ismasche#кидаем сетку в конф
config.ISCORNER = iscorner#кидаем углы в конф
config.ISLINE = isline    #кидаем линии в конф

config.WORK_PLACE = pol2 #обозначили рабочие поле

pol2.bind('<Button-1>', function.mouse_klick1)
pol2.bind('<Button-2>', function.mouse_klick2)


root.mainloop()
