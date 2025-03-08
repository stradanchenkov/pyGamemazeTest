import pygame
import random
import tkinter as tk
import random
import webbrowser
import pygame
import sys
import os

# Константы
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Инициализация pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лабиринт")

if getattr(sys, 'frozen', False):
    # Если программа запущена как EXE-файл
    audio_pathwin = os.path.join(sys._MEIPASS, "soundwin.mp3")
else:
    # Если программа запущена как скрипт
    audio_pathwin = "soundwin.mp3"

if getattr(sys, 'frozen', False):
    # Если программа запущена как EXE-файл
    audio = os.path.join(sys._MEIPASS, "buzz.mp3")
else:
    # Если программа запущена как скрипт
    audio = "buzz.mp3"

# Загружаем аудиофайл
pygame.mixer.music.load(audio_pathwin)


def Scream(count,speed):
    if count < 1000:
        root.geometry("500x300")
        root.geometry(f"+{(root.winfo_screenwidth() - 500) // 2}+{(root.winfo_screenheight() - 300) // 2}")
        count += 1
        root.after(speed, Scream2, count, speed)
        root.config(bg="black")


def Scream2(count,speed):
    if count < 1000 & speed > 5:
        root.geometry("1920x1080")
        root.geometry(f"+{(root.winfo_screenwidth() - 1920) // 2}+{(root.winfo_screenheight() - 1080) // 2}")
        root.config(bg="red")
        count += 1
        pygame.mixer.music.play()
        speed -= int(speed/10)
        root.after(speed, Scream, count, speed)
    else:
        txt1.destroy()
        webbrowser.open(f"https://youtu.be/FQSXOlkvWvY")
        root.destroy()
        pygame.quit()


def Yes_click():
    root.config(bg="gray")
    url = f"https://www.youtube.com/watch?v=Pn52veGd4AQ"
    webbrowser.open(url)
    root.destroy()

def No_click():
    root.config(bg="black")
    root.geometry("1280x720")
    root.geometry(f"+{(root.winfo_screenwidth() - 1280) // 2}+{(root.winfo_screenheight() - 720) // 2}")
    txt1.config(text="Жаль😔", font=("Arial",50), bg="black")
    txt1.pack(padx=50,pady=60)
    # Загружаем аудиофайл
    pygame.mixer.music.load(audio)
    root.after(1000, Scream, 1, 1000)
    Label.destroy()
    Yes.destroy()
    No.destroy()


# Класс для генерации лабиринта
class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[{"top": True, "bottom": True, "left": True, "right": True} for _ in range(cols)] for _ in range(rows)]
        self.generate_maze(0, 0)

    def generate_maze(self, row, col):
        directions = [("top", -1, 0), ("bottom", 1, 0), ("left", 0, -1), ("right", 0, 1)]
        random.shuffle(directions)

        for direction, dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and all(self.grid[new_row][new_col].values()):
                self.grid[row][col][direction] = False
                self.grid[new_row][new_col][{"top": "bottom", "bottom": "top", "left": "right", "right": "left"}[direction]] = False
                self.generate_maze(new_row, new_col)

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x, y = col * CELL_SIZE, row * CELL_SIZE
                if self.grid[row][col]["top"]:
                    pygame.draw.line(screen, WHITE, (x, y), (x + CELL_SIZE, y), 2)
                if self.grid[row][col]["bottom"]:
                    pygame.draw.line(screen, WHITE, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE), 2)
                if self.grid[row][col]["left"]:
                    pygame.draw.line(screen, WHITE, (x, y), (x, y + CELL_SIZE), 2)
                if self.grid[row][col]["right"]:
                    pygame.draw.line(screen, WHITE, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE), 2)

# Класс для игрока
class Player:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def move(self, dr, dc, maze):
        new_row, new_col = self.row + dr, self.col + dc
        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
            if dr == -1 and not maze.grid[self.row][self.col]["top"]:
                self.row = new_row
            elif dr == 1 and not maze.grid[self.row][self.col]["bottom"]:
                self.row = new_row
            elif dc == -1 and not maze.grid[self.row][self.col]["left"]:
                self.col = new_col
            elif dc == 1 and not maze.grid[self.row][self.col]["right"]:
                self.col = new_col

    def draw(self, screen):
        x = self.col * CELL_SIZE + CELL_SIZE // 2
        y = self.row * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, BLUE, (x, y), CELL_SIZE // 3)

# Создание лабиринта и игрока
maze = Maze(ROWS, COLS)
player = Player(0, 0)
end_row, end_col = ROWS - 1, COLS - 1

# Основной цикл игры
running = True
while running:
    screen.fill(BLACK)
    maze.draw(screen)

    # Отрисовка игрока
    player.draw(screen)

    # Отрисовка финиша
    pygame.draw.rect(screen, GREEN, (end_col * CELL_SIZE + CELL_SIZE // 4, end_row * CELL_SIZE + CELL_SIZE // 4, CELL_SIZE // 2, CELL_SIZE // 2))

    # Проверка на победу
    if player.row == end_row and player.col == end_col:
        root = tk.Tk()
        root.title("BEAST TEST!")
        root.geometry("640x480")
        root.geometry(f"+{(root.winfo_screenwidth() - 640) // 2}+{(root.winfo_screenheight() - 480) // 2}")
        root.attributes('-topmost', True)
        root.configure(bg="gray")
        root.resizable(width=False, height=False)
        txt1 = tk.Label(root, text="ВЫ ПОБЕДИЛИ!!!!🎉", font=("Arial", 30, "bold italic"), bg="gray", fg="white")
        txt1.pack(padx=50,pady=50)
        Label = tk.Label(root, text="Забрать приз?🎁", font=("Arial", 30, "bold italic"), bg="gray", fg="white")
        Label.pack(padx=50,pady=55)
        Yes = tk.Button(root, text="Да!", font=("Arial", 20, "bold"), width=6, height=1, command=Yes_click, bg="green", fg="white", activebackground="darkgreen", activeforeground="white")
        Yes.place(x=640 - 450, y=480 - 165)
        No = tk.Button(root, text="Нет", font=("Arial", 20, "bold"), width=6, height=1, command=No_click, bg="green", fg="white", activebackground="darkgreen", activeforeground="white")
        No.place(x=640 - 300, y=480 - 165)
        pygame.mixer.music.play()
        pygame.time.wait(3000)
        running = False
        root.mainloop()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.move(-1, 0, maze)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.move(1, 0, maze)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.move(0, -1, maze)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.move(0, 1, maze)
        pygame.display.flip()

pygame.quit()

#pyinstaller --noconsole --onefile --add-data "soundwin.mp3;." --add-data "buzz.mp3;." Game.py