import pyglet
import time
import datetime
from tkinter import *
from pyglet.media import *
import sys
import os


root = Tk()
root.geometry("430x450")
root.resizable(width=False, height=False)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title('Будильник')

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def start():
    try:
        hours = int(text_hour.get())
        minutes = int(text_minutes.get())
        timeForWaiting = hours * 3600 + minutes * 60 - int(time.strftime("%H", time.localtime())) * 3600 - int(time.strftime("%M", time.localtime())) * 60 - int(time.strftime("%S", time.localtime()))
        if timeForWaiting > -1 and (int(hours) <= 23 and int(minutes) <= 59):
            music = variable.get()
            l = Label(root, text=f'Установлен на {hours}:{minutes}',
                                bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=33, height=2)
            l.place(x=0, y=340)
            l = Label(root, text=f'Воспроизведется через {str(datetime.timedelta(seconds=timeForWaiting))} мин.',
                                bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=33, height=2)
            l.place(x=0, y=400)
            root.update()
            time.sleep(4)
            root.destroy()
            if(timeForWaiting>34):
                time.sleep(timeForWaiting-30)
            while True:
                 timeNow = time.strftime("%H:%M", time.localtime())
                 print(timeNow)
                 if (timeNow == hoursInStr(hours)+":"+minutesInStr(minutes)):
                     #path = resource_path(os.path.join('Music', f'{music}.mp3'))
                     music = pyglet.media.load(f'{music}.mp3', streaming=True)
                     music_player = Player()
                     music_player.queue(music)
                     music_player.volume = 0.2
                     music_player.play()
                     # music.play()
                     time.sleep(180)
                     close_program()
                 time.sleep(4)
        else:
            l = Label(root, text='Проверьте вводимые данные!',
                                bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=33, height=2)
            l.place(x=0, y=340)
    except:
        pass

def close_program():
    sys.exit()
def minutesInStr(minutes):
    minutesStr = str(minutes)
    if (minutes < 10):
        minutesStr = "0" + minutesStr
    return minutesStr
def hoursInStr(hours):
    hoursStr = str(hours)
    if (hours < 10):
        hoursStr = "0" + hoursStr
    return hoursStr


lbl = Label(root, text=f'Текущее время: {str(time.strftime("%H:%M:%S", time.localtime()))[:5]}',
                    bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=80, height=2)
lbl2 = Label(root, text='Установить будильник на:',
                    bg='#DA692F', fg='#000000', bd=2, font='Verdana', width=26, height=1)
hour = Label(root, text='Введите час',
                    bg='#DA692F', fg='#000000', bd=2, font='Verdana', width=15, height=1)
minutes = Label(root, text='Введите минуту',
                    bg='#DA692F', fg='#000000', bd=2, font='Verdana', width=15, height=1)
text_hour = Entry(root, bg='#CECECE', font='Cambria', justify='center', width=5)
text_minutes = Entry(root, bg='#CECECE', font='Cambria', justify='center', width=5)
btn = Button(text="⏰ Установить будильник ⏰", width=35, height=2, bg='#6EA6C1',
                        fg='#000000', font=('Verdana', 13, 'bold'), command=start)

miusik = Label(root, text=f'Выберете мелодию:',
                    bg='#FFCC00', fg='#000000', bd=2, font='Verdana', width=20, height=2)
btnExit = Button(root, text="Exit", bg="violet", width=20, font=40, command=close_program)
variable = StringVar(root)
shr = OptionMenu(root, variable, 'music1', 'music2', 'music3', 'music4', 'music5')


lbl.pack()
lbl2.place(x=0, y=60)
hour.place(x=45, y=100)
minutes.place(x=45, y=140)
text_hour.place(x=260, y=100)
text_minutes.place(x=260, y=140)
miusik.place(x=10, y=190)
shr.place(x=280, y=205)
btn.place(x=0, y=270)
btnExit.pack(side="bottom")
root.mainloop()