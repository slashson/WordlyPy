import customtkinter as ctk
from main import WordleGame, load_words

# Настройки CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Загружаем слова и создаем игру
words = load_words()
game = WordleGame(words)

# Создаем окно
app = ctk.CTk()
app.geometry("400x600")
app.title("Wordle на Python")

# Поле ввода
entry = ctk.CTkEntry(app, placeholder_text="Введите слово", justify="center")
entry.pack(pady=20, padx=40)

# Блок для отображения результатов
results_frame = ctk.CTkFrame(app)
results_frame.pack(pady=10)

# Сообщение о статусе
status_label = ctk.CTkLabel(app, text="")
status_label.pack(pady=10)

# Обработчик проверки слова
def check_guess():
    guess = entry.get().strip().lower()
    entry.delete(0, ctk.END)

    if len(guess) != len(game.secret_word):
        status_label.configure(text=f"❗ Введите слово из {len(game.secret_word)} букв")
        return

    result = game.match(guess)
    emoji = "".join(result)

    # Отображаем результат на экране (новая строка)
    label = ctk.CTkLabel(results_frame, text=emoji, font=("Consolas", 20))
    label.pack()

    # Проверка конца игры
    if game.is_won:
        status_label.configure(text="🎉 Победа! Ты угадал слово!")
        entry.configure(state="disabled")
    elif game.is_finished():
        status_label.configure(text=f"❌ Проиграл. Слово было: {game.get_secret_word()}")
        entry.configure(state="disabled")

# Кнопка проверки
check_button = ctk.CTkButton(app, text="Проверить", command=check_guess)
check_button.pack(pady=10)

# Запуск GUI
app.mainloop()