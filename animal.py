import os
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# அடிப்படை அமைப்பு
root = tk.Tk()
root.title("Animal Quiz")
root.geometry("500x650")

# உங்கள் சரியான பாத் (Path)
BASE_PATH = r"D:\animals"
animals = ["tiger", "zebra", "wolf", "starfish", "turtle", "whale", "turkey"]

score = 0
current_animal = ""

def next_question():
    global current_animal
    current_animal = random.choice(animals)
    
    # இமேஜ் பாத் - இதில் .jpg அல்லது .png என எது இருந்தாலும் தேடும்
    folder_path = os.path.join(BASE_PATH, current_animal)
    img_path = ""
    
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.lower().startswith(current_animal.lower()):
                img_path = os.path.join(folder_path, file)
                break
    
    try:
        img = Image.open(img_path)
        img = img.resize((400, 300))
        img_tk = ImageTk.PhotoImage(img)
        img_label.config(image=img_tk)
        img_label.image = img_tk
    except:
        messagebox.showerror("Error", f"{current_animal} படம் கிடைக்கவில்லை!")
        return

    options = random.sample(animals, 4)
    if current_animal not in options:
        options[0] = current_animal
    random.shuffle(options)

    for i in range(4):
        btn_text = options[i]
        option_buttons[i].config(text=btn_text.capitalize(), 
                                 command=lambda t=btn_text: check_answer(t))

def check_answer(guess):
    global score
    if guess == current_animal:
        score += 1
        messagebox.showinfo("Success", f"சரியான பதில்! ஸ்கோர்: {score}")
    else:
        messagebox.showerror("Wrong", f"தவறு! இது {current_animal.capitalize()}")
    next_question()

# UI Layout
img_label = tk.Label(root)
img_label.pack(pady=20)

tk.Label(root, text="இந்த விலங்கு எது?", font=("Arial", 16)).pack()

option_buttons = []
for _ in range(4):
    btn = tk.Button(root, text="", font=("Arial", 12), width=20, pady=5)
    btn.pack(pady=5)
    option_buttons.append(btn)

next_question()
root.mainloop()
