import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x400")
root.configure(bg="black")

def navigate_to_page1():
    # Code to navigate to Page 1
    label.config(text="You are on Page 1")
    home_button.pack(side="bottom", anchor="se")
    fruits_label.pack()
    fruits_dropdown.pack()
    

def navigate_to_page2():
    # Code to navigate to Page 2
    label.config(text="You are on Page 2")
    home_button.pack(side="bottom", anchor="se")
    fruits_label.pack_forget()
    fruits_dropdown.pack_forget()
    

def navigate_to_home():
    # Code to navigate to Home Page
    label.config(text="Welcome to the Home Page")
    home_button.pack_forget()
    fruits_label.pack_forget()
    fruits_dropdown.pack_forget()

def search_fruits(*args):
    search_term = fruits_dropdown.get()
    matching_fruits = [fruit for fruit in fruits if search_term.lower() in fruit.lower()]
    fruits_dropdown['values'] = matching_fruits
    if len(matching_fruits) == 1:
        new_window = tk.Toplevel(root)
        new_window.geometry("400x400")
        new_label = tk.Label(new_window, text=f"You selected {matching_fruits[0]}", bg="black", fg="white")
        new_label.pack(pady=20)
        new_button = tk.Button(new_window, text="Close", bg="white", width=10, height=2, command=new_window.destroy)
        new_button.pack(pady=10)
    

frame = tk.Frame(root, bg="grey", width=350, height=200, pady=10)
frame.pack(side="top", pady=50, anchor="center")

button1 = tk.Button(frame, text="Button 1", bg="white", width=20, height=2, command=navigate_to_page1)
button1.pack(side="left", padx=10)

button2 = tk.Button(frame, text="Button 2", bg="white", width=20, height=2, command=navigate_to_page2)
button2.pack(side="right", padx=10)

label = tk.Label(root, text="Welcome to the Home Page", bg="black", fg="white")
label.pack(pady=20)

home_button = tk.Button(root, text="Home", bg="white", width=10, height=2, command=navigate_to_home)

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew", "Iced Melon", "Jackfruit",
          "Kiwi", "Lemon", "Mango", "Nectarine", "Orange", "Papaya", "Quince", "Raspberry", "Strawberry", "Tomato"]

fruits_label = tk.Label(root, text="Fruits", bg="black", fg="white")
fruits_dropdown = ttk.Combobox(root, values=fruits, width=30)
fruits_dropdown.bind("<KeyRelease>", search_fruits)
#fruits_dropdown.pack()

root.mainloop()