import customtkinter as ctk
from customtkinter import CTkFrame
from PIL import Image

class Keyboard():
    def __init__(self, screen, crdx, crdy, on_type=None):
        self.screen = screen

        self.crdx = crdx
        self.crdy = crdy

        self.text = []

        self.on_type = on_type

        self.show()

    def add_letter(self, letter):
        if len(self.text) < 4:  # ограничение можно оставить, если хочешь
            self.text.append(letter)
            if self.on_type:
                self.on_type("".join(self.text))  # всегда передаём полное слово

    def delete_letter(self):
        if self.text:
            self.text.pop()
            if self.on_type:
                self.on_type("".join(self.text))

    def show(self):
        letters = 'QWERTYUIOP'
        letters_r2 = 'ASDFGHJKL'
        letters_r3 = 'ZXCVBNM'

        self.frame = CTkFrame(self.screen, fg_color='#393738')
        self.frame.place(relx=self.crdx, rely=self.crdy, anchor='c')

        for i in range(len(letters)):
            btn = ctk.CTkButton(self.frame,
                                fg_color='#646464',
                                text=letters[i],
                                font=('SF Pro', 18),
                                corner_radius=8,
                                width=51,
                                height=51,
                                command=lambda l=letters[i]: self.add_letter(l))
            btn.grid(row = 0, column = i, padx=1, pady=1)

        for i in range(len(letters_r2)):
            btn = ctk.CTkButton(self.frame,
                                fg_color='#646464',
                                text=letters_r2[i],
                                font=('SF Pro', 18),
                                corner_radius=8,
                                width=51,
                                height=51,
                                command=lambda l=letters_r2[i]: self.add_letter(l))
            btn.grid(row = 1, column = i, padx=1, pady=1)


        for i in range(len(letters_r3)):
            btn = ctk.CTkButton(self.frame,
                                fg_color='#646464',
                                text=letters_r3[i],
                                font=('SF Pro', 18),
                                corner_radius=8,
                                width=51,
                                height=51,
                                command=lambda l=letters_r3[i]: self.add_letter(l))
            btn.grid(row = 2, column = i+1, padx=1, pady=1)

        self.delete_icon = ctk.CTkImage(
            light_image=Image.open("icons/delete_icon.png"),
            dark_image=Image.open("icons/delete_icon.png"),
            size=(28, 28))

        delete_btn = ctk.CTkButton(self.frame,
                                fg_color='#0f77f0',
                                image=self.delete_icon,
                                text='',
                                corner_radius=8,
                                width=102,
                                height=51,
                                command=self.delete_letter)
        delete_btn.grid(row = 2, column = i+2, padx=1, pady=1, columnspan=2)

# root = ctk.CTk()
# app = Keyboard(root)
# root.mainloop()