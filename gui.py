import customtkinter as ctk
from keyboard import Keyboard
from main import match, load_word, random_choise, results
import random
from keyboard import Keyboard

class WorldlyApp:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry('550x750')
        self.screen.title('WorldlyPY')
        self.screen.configure(fg_color='#211F20')
        self.secret_word = None
        self.current_row = 0
        self.current_coulmn = 0

        self.user_guesses = None
        self.temp_text = []

        self.play_screen()

    def play_screen(self):
        self.clear_screen()

        self.choose_secret_word(secret_word=random_choise())
        self.frame = ctk.CTkFrame(self.screen, fg_color='#211F20')
        self.frame.place(relx=0.5, y=250, anchor='center')
        # ctk.CTkLabel(frame, text="Register", width=50, height=50, font=("SF Pro", 25, "bold")).pack(padx=130, pady=20)
        self.playground(screen=self.screen)

    def clear_screen(self):
        for widget in self.screen.winfo_children():
            widget.destroy()
    def choose_secret_word(self, secret_word):
        self.secret_word = secret_word
        print(f'The secret word : {self.secret_word}')

# UI Shit
    def playground(self, screen):
        self.screen = screen
        self.entries = [[None for _ in range(4)] for _ in range(5)]

        for row in range(5):
            for col in range(4):
                entry = ctk.CTkButton(self.frame,
                                      width=75,
                                      height=75,
                                      anchor='center',
                                      fg_color='#211F20',
                                      hover_color='#211F20',
                                      border_color='#4D4D4D',
                                      border_width=4,
                                      corner_radius=14,
                                      text='',
                                      state="disabled")
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.entries[row][col] = entry

        self.keyboard = Keyboard(self.screen,0.5, 0.88, on_type=self.handle_typing)

    def handle_typing(self, word):
        word = word.upper()

        for i, letter in enumerate(word):
            self.entries[self.current_row][i].configure(text=letter,
                                                        font=('SF Pro', 20),
                                                        text_color_disabled='white')

        if len(word) == 4:
            result = match(list(word.lower()), self.secret_word)

            for i in range(4):
                color = result[i].strip()
                if color == 'g':
                    bg = '#00A878'
                elif color == 'y':
                    bg = '#FFD447'
                else:
                    bg = '#3A3A3C'

                self.entries[self.current_row][i].configure(fg_color=bg)

            self.keyboard.text = []

            self.current_row += 1

'''как сделать изменение квадратиков в зависимости от results'''
'''Add Lose Screen, show guessed word, restart button'''
'''Add Win Screen, new game button, auto restart in 5 sec'''
root = ctk.CTk()
app = WorldlyApp(root)
root.mainloop()