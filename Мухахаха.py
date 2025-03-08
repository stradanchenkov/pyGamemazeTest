import tkinter as tk
import random
import time
import webbrowser
import pygame
import sys
import os

# Инициализация pygame
pygame.init()

# Путь к аудиофайлу
if getattr(sys, 'frozen', False):
    # Если программа запущена как EXE-файл
    audio_path = os.path.join(sys._MEIPASS, "sound.mp3")
else:
    # Если программа запущена как скрипт
    audio_path = "sound.mp3"

# Загружаем аудиофайл
pygame.mixer.music.load(audio_path)

def move_button_smoothly(button, target_x, target_y, step=10):
    # Получаем текущие координаты кнопки
    current_x = button.winfo_x()
    current_y = button.winfo_y()

    # Вычисляем разницу между текущими и целевыми координатами
    dx = target_x - current_x
    dy = target_y - current_y

    # Если кнопка уже на месте, выходим из функции
    if dx == 0 and dy == 0:
        return

    # Вычисляем новые координаты с учетом шага
    new_x = current_x + (dx / step)
    new_y = current_y + (dy / step)

    # Перемещаем кнопку на новые координаты
    button.place(x=int(new_x), y=int(new_y))

    # Планируем следующий шаг анимации через 10 мс
    root.after(5, move_button_smoothly, button, target_x, target_y, step)

def move_button(event):
    target_x = random.randint(50, root.winfo_width() - No.winfo_width())
    target_y = random.randint(50, root.winfo_height() - No.winfo_height())
    move_button_smoothly(No, target_x, target_y)



def on_click_button():
    root.config(bg="black")
    Label.config(text="Ну я так и знал! :}", bg="black", fg="red")
    Label.place(x=80, y=80)
    Yes.destroy()
    No.destroy()
    # Воспроизводим звук
    pygame.mixer.music.play()
    url = f"https://rutube.ru/video/1118e8a40f44de0e479edf0108d80fa9/"
    webbrowser.open(url)
    root.after(speed, Scream, 1)

def Scream(count):
    if count < 1000:
        root.geometry("500x300")
        root.geometry(f"+{(root.winfo_screenwidth() - 500) // 2}+{(root.winfo_screenheight() - 300) // 2}")
        Label.place(x=80, y=80)
        count += 1
        root.after(speed, Scream2, count)
        Label.config(bg="white")
        root.config(bg="black")


def Scream2(count):
    if count < 1000:
        root.geometry("1920x1080")
        root.geometry(f"+{(root.winfo_screenwidth() - 1920) // 2}+{(root.winfo_screenheight() - 1080) // 2}")
        Label.config(bg="black")
        root.config(bg="white")
        Label.place(x=180, y=180)
        count += 1
        root.after(speed, Scream, count)
    else:
        root.destroy()

def Scream3(count):
        if count < 1000:
            root.geometry("1280x720")
            root.geometry(f"+{(root.winfo_screenwidth() - 1280) // 2}+{(root.winfo_screenheight() - 720) // 2}")
            Label.config(bg="blue")
            root.config(bg="red")
            Label.place(x=380, y=380)
            count += 1
            root.after(speed, Scream, count)

def Screen2():

    Label.config(text="Ты гей?")
    Yes.config(text="Да", font=("Arial", 20, "bold"), width=6, height=1, command=on_click_button, bg="green", fg="white", activebackground="darkgreen", activeforeground="white")
    Yes.place(x=120, y=165)
    No.config(text="Нет", font=("Arial", 20, "bold"), width=6, height=1, command=move_button("<Punch>"), bg="red", fg="white")
    No.place(x=265, y=165)
    No.bind("<Enter>", move_button)

def Main():
    time.sleep(1)
    root = tk.Tk()
    root.title("BEAST TEST!")
    root.geometry("1920x1080")
    root.geometry(f"+{(root.winfo_screenwidth() - 1920) // 2}+{(root.winfo_screenheight() - 1080) // 2}")
    root.attributes('-topmost', True)
    root.configure(bg="black")
    root.resizable(width=False, height=False)
    Label = tk.Label(root, text="У вас 0 IQ Вы немошь ебаный", font=("Arial", 80, "bold italic"), bg="black", fg="red")
    Label.place(x=100, y=100)



speed = 20

root = tk.Tk()
root.title("BEAST TEST!")
root.geometry("500x300")
root.geometry(f"+{(root.winfo_screenwidth() - 500) // 2}+{(root.winfo_screenheight() - 300) // 2}")
root.attributes('-topmost', True)
root.configure(bg="gray")
root.resizable(width=False, height=False)

Label = tk.Label(root, text="Начать тест?", font=("Arial", 30, "bold italic"), bg="gray", fg="white")
Label.place(x=100, y=20)

Yes = tk.Button(root, text="Да!", font=("Arial", 20, "bold"), width=6, height=1, command=Screen2, bg="green", fg="white", activebackground="darkgreen", activeforeground="white")
Yes.place(x=100, y=165)

No = tk.Button(root, text="нет иди нахуй", font=("Arial", 20, "bold"), width=12, height=1, command=Main, bg="red", fg="white", activebackground="darkgreen", activeforeground="white")
No.place(x=245, y=165)

root.mainloop()
#pyinstaller --noconsole --onefile --add-data "sound.mp3;."