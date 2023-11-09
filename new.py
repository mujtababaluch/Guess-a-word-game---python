import random
import tkinter as tk
from tkinter import ttk

easy_words = [
    "hello",
    "world",
    "python",
    "java",
    "html",
    "css",
    "javascript",
    "variable",
    "function",
    "string",
    "array",
    "loop",
    "boolean",
    "if",
    "else",
    "print",
    "input",
    "file",
    "list",
    "dictionary"
]

medium_words = [
    "algorithm",
    "object",
    "class",
    "inheritance",
    "polymorphism",
    "encapsulation",
    "interface",
    "exception",
    "debug",
    "database",
    "query",
    "framework",
    "module",
    "package",
    "recursion",
    "sorting",
    "searching",
    "stack",
    "queue",
    "pointer"
]

hard_words = [
    "concurrency",
    "parallelism",
    "memory",
    "cache",
    "os",
    "kernel",
    "virtualization",
    "security",
    "networking",
    "protocol",
    "authentication",
    "authorization",
    "cryptography",
    "blockchain",
    "ml",
    "ai",
    "bigdata",
    "datascience",
    "quantum",
    "iot"
]




def check_guess():
    guess = entry_guess.get()
    entry_guess.delete(0, tk.END)
    if not guess:
        return

    global user_guess, chance
    if guess in r_word:
        user_guess += guess
        guessed_word = ' '.join([ch if ch in user_guess else '_' for ch in r_word])
        label_word.config(text=guessed_word)
        if '_' not in guessed_word:
            output.set(f"You win! The word was '{r_word}'")
            entry_guess.config(state='disabled')
    else:
        chance -= 1
        output.set(f"Wrong guess! {chance} chances left")
        if chance == 0:
            output.set(f"Game Over! The word was '{r_word}'")
            entry_guess.config(state='disabled')

def start_game():
    global r_word, user_guess, chance
    r_word = random.choice(easy_words + medium_words + hard_words)
    user_guess = ''
    chance = 5
    guessed_word = ' '.join(['_' for _ in r_word])
    label_word.config(text=guessed_word)
    entry_guess.config(state='normal')
    entry_guess.focus_set()

    if r_word in easy_words:
        hint = f"Hint: It is an Easy word related to programming and consists of {len(r_word)} letters"
    elif r_word in medium_words:
        hint = f"Hint: It is a Medium word related to programming and consists of {len(r_word)} letters"
    elif r_word in hard_words:
        hint = f"Hint: It is a Hard word and related to programming consists of {len(r_word)} letters"
    else:
        hint = ""

    label_hint.config(text=hint)
    output.set("")

root = tk.Tk()
root.title("Word Guessing Game")

style = ttk.Style()
style.configure("TButton",
                padding=10,
                font=('Arial', 12),
                foreground="black",
                background="black",
                activeforeground="white",
                activebackground="#55a15e")
                
style.map("TButton",
          foreground=[('active', 'black')],
          background=[('!disabled', '#4CAF50'), ('active', '#55a15e')])


style.configure("TLabel",
                font=('Arial', 14),
                padding=10)
style.configure("TEntry",
                font=('Arial', 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack()

label_title = ttk.Label(main_frame, text="Word Guessing Game")
label_title.pack()

label_hint = ttk.Label(main_frame, text="")
label_hint.pack()

label_word = ttk.Label(main_frame, text="Press 'Start New Game' to begin")
label_word.pack()

entry_guess = ttk.Entry(main_frame)
entry_guess.pack()

button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=15)  # Add margin-top to button_frame

button_guess = ttk.Button(button_frame, text="Guess", command=check_guess, style="TButton")
button_guess.pack(side=tk.LEFT, padx=5)

button_start = ttk.Button(button_frame, text="Change The Word", command=start_game, style="TButton")
button_start.pack(side=tk.LEFT, padx=5)

output = tk.StringVar()
output.set("")
label_output = ttk.Label(main_frame, textvariable=output)
label_output.pack()

entry_guess.config(state='disabled')

start_game()

root.mainloop()
