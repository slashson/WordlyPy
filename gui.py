import customtkinter as ctk
from customtkinter import CTkFrame

from main import match, load_word, random_choise
import random


class WorldlyApp:
    def __init__(self, screen):
        self.screen = screen
        self.screen.geometry('550x750')
        self.screen.title('WorldlyPY')
        self.screen.configure(fg_color='#211F20')
        self.secret_word = None


        self.play_screen()

    def play_screen(self):
        self.clear_screen()

        self.choose_secret_word(secret_word=random_choise())
        self.frame = ctk.CTkFrame(self.screen, fg_color='#211F20')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')
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
        entries = [[None for _ in range(4)] for _ in range(5)]

        for row in range(5):
            for col in range(4):
                entry = ctk.CTkButton(self.frame,
                                      width=87,
                                      height=87,
                                      anchor='center',
                                      fg_color='#211F20',
                                      hover_color='#211F20',
                                      border_color='#4D4D4D',
                                      border_width=4,
                                      corner_radius=13,
                                      text='')
                entry.grid(row=row, column=col, padx=5, pady=5)
                entries[row][col] = entry
'''Add Lose Screen, restart button'''
'''Add Win Screen, new game button'''
root = ctk.CTk()
app = WorldlyApp(root)
root.mainloop()