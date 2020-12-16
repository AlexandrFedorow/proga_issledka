
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter.filedialog import *
from math import *

import re
import config
import creations_objects as create_object


def read_file(name):
    file = open(str(name))
    values = file.read().split("\n")
    data = []

    for key in values:
        value = re.findall(r"[-+]?\d*\.\d+|\d+", key)
        if value != []:
            data.append(value)
    file.close()

    for i in range(len(data)):
        for j in range(2):
            data[i][j] = float(data[i][j])
    data.append(data[0])
    config.DATA = data
    return data


def paint(name, mod=1):#ставит точки
    try:
        config.WORK_PLACE.delete(config.POINT)
        config.WORK_PLACE.delete(config.LINE)
        if mod == 1:
            coordinate = read_file(name)
        elif mod == 3:
            coordinate = config.MAIN_DATA
            coordinate.append(config.MAIN_DATA[len(config.MAIN_DATA)-1])
        else:
            coordinate = config.DATA

        for i in range(len(coordinate)-1):
            p = create_object.Point(coordinate[i][0] * config.SIZE + config.SHIFT_X, coordinate[i][1] * config.SIZE + config.SHIFT_Y, "#1f1", config.POINT, config.WORK_PLACE)
            p.create_point()
    except IndexError:
        messagebox.showinfo("Сообщение об ошибке:", "Ошибка открытия файла \n Файл не обнаружен.")


def draw_line(mod=2):#чертит линии по точкам
    config.WORK_PLACE.delete(config.LINE)
    if mod == 2:
        coordinate = config.DATA
    else:
        coordinate = config.MAIN_DATA
    for i in range(len(coordinate)-1):
        line = create_object.Line(coordinate[i][0] * config.SIZE + config.SHIFT_X, coordinate[i][1] * config.SIZE + config.SHIFT_Y, coordinate[i+1][0] * config.SIZE + config.SHIFT_X, coordinate[i+1][1]* config.SIZE + config.SHIFT_Y, '#FFF', config.LINE, config.WORK_PLACE)
        line.create_line()


def open_schema():
    try:
        config.MAIN_DATA = [] #обнуляем углы багфикс
        config.MODE = 1#ставим режим для отрисовки из файла
        config.POINTS_OR_LINES = 1#при открытии выставляет точки
        dir_path = askopenfilename()
        config.DIR_PATH = dir_path
        paint(dir_path, config.MODE)
        config.MODE = 2
    except IOError:
        messagebox.showinfo("Сообщение об ошибке:", "Ошибка открытия файла \n Попробуйте снова.")


def save():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*")))


def increase():
    try:
        config.WORK_PLACE.delete('ms')
        config.MASCHE_SCALE += 15
        create_object.Masche(config.WORK_PLACE, config.MASCHE_SCALE, config.MASCHE_MODE)

        config.SIZE += 0.5
        config.SCALE.set(config.SIZE)
        config.FORM_CHEK += 0.5

        config.INCREASE_CHEK += 1

        if config.INCREASE_CHEK == 8:
            config.INCREASE_CHEK = 4
            value = []
            for i in range(len(config.DATA)-1):
                a = []
                value.append(config.DATA[i])
                a.append((config.DATA[i][0] + config.DATA[i+1][0]) / 2)
                a.append((config.DATA[i][1] + config.DATA[i+1][1]) / 2)
                value.append(a)

            a = []
            a.append((config.DATA[len(config.DATA)-1][0] + config.DATA[0][0]) / 2)
            a.append((config.DATA[len(config.DATA)-1][1] + config.DATA[0][1]) / 2)
            value.append(a)
            config.DATA = value
        if config.POINTS_OR_LINES == 1:
            paint(1, config.MODE)
        else:
            draw_line(config.MODE)
    except IndexError:
        config.WORK_PLACE.delete('ms')
        config.MASCHE_SCALE += 15
        create_object.Masche(config.WORK_PLACE, config.MASCHE_SCALE, config.MASCHE_MODE)


def reducee():
    try:
        config.WORK_PLACE.delete('ms')
        config.MASCHE_SCALE -= 15
        create_object.Masche(config.WORK_PLACE, config.MASCHE_SCALE, config.MASCHE_MODE)

        config.SIZE -= 0.5
        config.SCALE.set(config.SIZE)
        config.FORM_CHEK -= 0.5

        config.INCREASE_CHEK -= 1

        if config.INCREASE_CHEK == 0:
            config.INCREASE_CHEK = 4

            for i in range(len(config.DATA)):
                if i % 2 != 0:
                    config.DATA[i] = ['d', 'd']

            i = 0
            while i < len(config.DATA):
                if config.DATA[i][0] == 'd':
                    del config.DATA[i]
                else:
                    i += 1
        if config.POINTS_OR_LINES == 1:
            paint(1, config.MODE)
        else:
            draw_line(config.MODE)
    except FileNotFoundError:
        messagebox.showinfo("Сообщение об ошибке:", "Ошибка")


def left():
    try:
        config.SHIFT_X -= 5
        if config.POINTS_OR_LINES == 1:
            paint(1, config.MODE)
        else:
            draw_line(config.MODE)

    except FileNotFoundError:
        messagebox.showinfo("Сообщение об ошибке:", "Ошибка")


def right():
    try:
        config.SHIFT_X += 5
        if config.POINTS_OR_LINES == 1:
            paint(1, config.MODE)
        else:
            draw_line(config.MODE)
    except FileNotFoundError:
        messagebox.showinfo("Сообщение об ошибке:", "Ошибка")


def upper():
    try:
        config.SHIFT_Y -= 5
        if config.POINTS_OR_LINES == 1:
            paint(1, config.MODE)
        else:
            draw_line(config.MODE)
    except FileNotFoundError:
        messagebox.showinfo("Сообщение об ошибке:", "Ошибка")


def down():
    try:
        config.SHIFT_Y += 5
        if config.POINTS_OR_LINES == 1:
            paint(1, config.MODE)
        else:
            draw_line(config.MODE)
    except FileNotFoundError:
        messagebox.showinfo("Сообщение об ошибке:", "Ошибка")


def corner():#находит углы
    config.MAIN_DATA = []
    dx2 = 0
    dy2 = 0
    for i in range(len(config.DATA)-1):
        dy1 = config.DATA[i+1][1] - config.DATA[i][1]
        dx1 = config.DATA[i+1][0] - config.DATA[i][0]

        if dx1 != dx2 or dy1 != dy2:
            config.MAIN_DATA.append(config.DATA[i])

        dx2 = dx1
        dy2 = dy1

    config.MAIN_DATA.append(config.MAIN_DATA[0])


def apply():
    chek1 = config.ISMASCHE.get()
    chek2 = config.ISCORNER.get()
    chek3 = config.ISLINE.get()

    scale_chek = float(config.SCALE.get())
    config.FORM_CHEK = float(config.FORM_CHEK)

    if scale_chek >= config.FORM_CHEK and scale_chek >= 1:
        for i in range(int((scale_chek - config.FORM_CHEK) / 0.5)):
            increase()
        config.FORM_CHEK = scale_chek

    elif scale_chek <= config.FORM_CHEK and scale_chek >= 1:
        for i in range(int((config.FORM_CHEK - scale_chek) / 0.5)):
            reducee()
        config.FORM_CHEK = scale_chek

    if chek1 == 0:
        config.WORK_PLACE.delete('ms')
        config.MASCHE_MODE = 0
    else:
        config.MASCHE_MODE = 1
        create_object.Masche(config.WORK_PLACE, config.MASCHE_SCALE)
        paint(1, config.MODE)

    if chek2 == 1:
        corner()
        config.MODE = 3
        paint('', config.MODE)
    else:
        config.MODE = 2
        paint('', config.MODE)

    if chek3 == 1:
        config.POINTS_OR_LINES = 0
        config.WORK_PLACE.delete(config.POINT)
        draw_line(config.MODE)
    else:
        config.POINTS_OR_LINES = 1
        paint('', config.MODE)
        config.WORK_PLACE.delete(config.LINE)


def help():
    messagebox.showinfo("Help", "The program only opens files of the format .txt")


def mouse_klick1(event):
    x = event.x
    y = event.y
    p = create_object.Point(x-5, y-7, '#ff7e00', config.WIDTH_POINT, config.WORK_PLACE)
    scale = float(config.SCALE.get())

    if config.WIDTH_POINTS_CTR != 2:
        if config.WIDTH_POINTS_CTR == 0:
            config.X_Y[0][0] = x
            config.X_Y[0][1] = y

        if config.WIDTH_POINTS_CTR == 1:
            config.X_Y[1][0] = x
            config.X_Y[1][1] = y

        p.create_point()
        config.WIDTH_POINTS_CTR += 1
    else:

        width = sqrt((config.X_Y[1][0] - config.X_Y[0][0])**2 + (config.X_Y[1][1] - config.X_Y[0][1])**2) / scale
        messagebox.showinfo("Width", "width " + "%.2f" % width + " m")

        config.WIDTH_POINTS_CTR = 0
        config.WORK_PLACE.delete(config.WIDTH_POINT)


def mouse_klick2(event):
    config.WORK_PLACE.delete(config.WIDTH_POINT)
    config.WIDTH_POINTS_CTR = 0
