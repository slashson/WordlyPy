# 🌍 WorldlyPY

**WorldlyPY** is a mini-game inspired by **Wordle**, built with Python and a graphical interface using `customtkinter`.  
The player must guess a random 4-letter English word in 5 attempts using an on-screen keyboard.

---

## 🎮 How to Play

- Use the on-screen keyboard to input words.
- Each guess must be exactly **4 letters**.
- After every attempt, each letter box will change color:
  - 🟩 Green — correct letter in the **correct position**.
  - 🟨 Yellow — letter exists but in the **wrong position**.
  - ⬛ Gray — letter is **not in the word**.
- You have **5 attempts** to guess the word!

---

## 🧩 Features

- Full **GUI interface** using `customtkinter`
- Responsive **on-screen keyboard**
- Random word loading from `words.txt`
- Visual feedback with color-coded buttons
- Win/lose detection and game restart
- Modular and scalable codebase
  
---

## 🧠 Under the Hood

This project demonstrates clean **Python OOP (Object-Oriented Programming)** practices with:

- ✅ Class-based architecture (`WorldlyApp`, `Keyboard`)
- ✅ GUI layout built with **`customtkinter`** (a modern wrapper around `tkinter`)
- ✅ Use of **encapsulation**, **callback functions**, and **modularity**
- ✅ Separation of logic and interface (`main.py` handles logic, `gui.py` handles UI)
- ✅ Event-driven design (button presses update game state dynamically)
- ✅ Basic file I/O (reading from `words.txt`)
- ✅ Manual control of GUI components (text fields, colors, grid)

This makes the code easy to maintain, extend, and read.

---

# 📁 Project Structure

WorldlyPY/
├── gui.py           # Main GUI controller
├── keyboard.py      # Custom on-screen keyboard class
├── main.py          # Game logic: matching and word selection
├── words.txt        # Dictionary of 4-letter words
├── icons/
│   └── delete_icon.png  # Delete key icon
└── README.md

---

## 🚀 How to Run

1. Install the required libraries:

```bash
pip install customtkinter pillow

python gui.py
```

🛠 Dependencies
	•	Python 3.10+
	•	customtkinter
	•	Pillow (for loading images)

📚 Future Plans
	•	Support for 5- or 6-letter words
	•	Game statistics
	•	Physical keyboard input support

Built from scratch for learning

