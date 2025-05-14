import customtkinter as ctk
from main import match, load_word, random_choise
import random


def check_guess():
    pass


def user_guess():
    pass



results = ['' for i in range(5)]

# Настройка окна
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("400x600")
app.title("Wordle GUI")

# Ввод
entry = ctk.CTkEntry(app, placeholder_text="Введите слово")
entry.pack(pady=20)

# Результаты
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

button = ctk.CTkButton(app, text="Проверить", command=check_guess)
button.pack(pady=10)



app.mainloop()

# Загрузка слов
load_word()
print(clean_lines)
random_choise()