import tkinter as tk
from tkinter import ttk
import pandas as pd

root = tk.Tk()
root.geometry("400x400")
root.configure(bg="black")


def navigate_to_page1():
    global selection_frame
    global ev_num
    global sid_num
    global confirm_button
    global sid_val
    global ev_val
    global sid_text

    # Code to navigate to Page 1
    label.config(text="Risk Report")
    home_button.pack(side="bottom", anchor="se")
    risk_button.pack_forget()
    hist_button.pack_forget()
    frame.pack_forget()

    # Add yes/no button
    selection_label.pack(pady=10)
    selection_frame = tk.Frame(root,bg="black")
    selection_frame.pack()
    selection_var = tk.BooleanVar()
    selection_var.set(False)
    yes_button = tk.Radiobutton(selection_frame, bg="grey", fg="black", text="Yes", variable=selection_var, value=True, command=lambda: ev_num.config(state="normal"))
    yes_button.pack(side="left")
    no_button = tk.Radiobutton(selection_frame, bg="grey", fg="black", text="No", variable=selection_var, value=False, command=lambda: ev_num.config(state="disabled", text="0"))
    no_button.pack(side="left", padx=10)

    # Add text box for input that is affected by Yes/No
    def validate_input(text):
        if text.isdigit():
            if 0 <= int(text) <= 10000:
                return True
        elif text == "":
            return True
        return False

    ev_var = tk.StringVar()
    ev_var.trace_add("write", lambda *args: ev_var.set("".join(filter(str.isdigit, ev_var.get()))[:5]))
    ev_num = tk.Entry(root, textvariable=ev_var, validate="key")
    ev_num.config(validatecommand=(ev_num.register(validate_input), '%P'))
    ev_num.pack(pady=10)

    def input_selected():
        if selection_var.get():
            ev_num.config(state="normal")
        else:
            ev_num.config(state="disabled", text="0")

    # Add text box for input that is not affected by Yes/No
    def validate_sid_num(text):
        if text.isdigit():
            if 0 <= int(text) <= 99999999:
                return True
        elif text == "":
            return True
        return False

    sid_val = tk.StringVar()
    sid_val.set("")
    sid_text = tk.Label(root,bg="black", fg="white", text="Please enter transformer SID number.")
    sid_text.pack()
    sid_num = tk.Entry(root, textvariable=sid_val, validate="key")
    sid_num.config(validatecommand=(sid_num.register(validate_sid_num), '%P'))
    sid_num.pack(pady=10)

    # Add button to confirm input selection
    confirm_button = tk.Button(root, text="Confirm", bg="white", width=10, height=2, command=lambda: [input_selected(), save_inputs()])
    confirm_button.pack(pady=10)

    # Pack button and input boxes
    input_selected()  # Disable input box initially

    def save_inputs():
        global sid_val
        global ev_val
        sid_val = sid_num.get()
        ev_val = ev_num.get()
        if not selection_var.get():
            ev_val = "0"
        print(int(sid_val))
        print(int(ev_val))
'''    
def riskRun_analysis():
    numEvs = ev_count_entry.get()
    xfmrSID = transformer_entry.get()
    print(f"KVA Rating: {numEvs}")
    print(f"Sim EV: {xfmrSID}")
'''
def navigate_to_page2():
    # Code to navigate to Page 2
    label.config(text="You are on Page 2")
    home_button.pack(side="bottom", anchor="se")
    risk_button.pack_forget()
    hist_button.pack_forget()
    frame.pack_forget()

    # Add input fields for KVA Rating and Sim EV
    kva_label.pack(pady=10)
    kva_entry.pack(pady=5)
    sim_label.pack(pady=10)
    sim_entry.pack(pady=5)
    run_button.pack(pady=10)
    
     

# Add a "Run" button
def run_analysis():
    #global text_widget
    kva_rating = kva_entry.get()
    sim_ev = sim_entry.get()
    print(f"KVA Rating: {kva_rating}")
    print(f"Sim EV: {sim_ev}")

    # Code to navigate to the new page
    label.config(text="You are on the Results Page")
    home_button.pack(side="bottom", anchor="se")
    risk_button.pack_forget()
    hist_button.pack_forget()
    frame.pack_forget()
    kva_label.pack_forget()
    kva_entry.pack_forget()
    sim_label.pack_forget()
    sim_entry.pack_forget()
    run_button.pack_forget()
    image_label.pack(pady=20)
    
    # Read the CSV file
    csv_path = r"C:/Users/mbleu/Desktop/vscode/example.csv" # replace with your own CSV file path
    df = pd.read_csv(csv_path)

    # Display the CSV file in a Text widget
    text_widget = tk.Text(root, height=20, width=100)
    text_widget.insert("1.0", df.to_string(index=False))
    text_widget.pack(pady=20)
    
    # Add a label to display the results
    #results_label = tk.Label(root, text=f"Results:\nKVA Rating: {kva_rating}\nSim EV: {sim_ev}", bg="black", fg="white", justify="left")
    #results_label.pack(side="top", pady=50, anchor="center")

def navigate_to_home():
    # Code to navigate to Home Page
    label.config(text="EPB Transformer Load Analysis")
    home_button.pack_forget()
    risk_button.pack(side="left", padx=10)
    hist_button.pack(side="right", padx=10)
    frame.pack(side="top", pady=50, anchor="center")
    kva_label.pack_forget()
    kva_entry.pack_forget()
    sim_label.pack_forget()
    sim_entry.pack_forget()
    run_button.pack_forget()
    image_label.pack_forget()
    selection_label.pack_forget()
    selection_frame.pack_forget()
    ev_num.pack_forget()
    confirm_button.pack_forget()
    sid_num.pack_forget()
    sid_text.pack_forget()

    

frame = tk.Frame(root, bg="grey", width=350, height=200, pady=10)
frame.pack(side="top", pady=50, anchor="center")

"""image_path = r"C:/Users/mbleu/Desktop/vscode/Histogram_Report.png"
image = tk.PhotoImage(file=image_path)
image_label = tk.Label(root, image=image)"""

kva_label = tk.Label(root, text="KVA Rating:", bg="black", fg="white")

kva_entry = tk.Entry(root, bg="white", width=30)

sim_label = tk.Label(root, text="Sim EV (0 - 10,000):", bg="black", fg="white")

sim_entry = tk.Entry(root, bg="white", width=30)


run_button = tk.Button(root, text="Run", bg="white", width=10, height=2, command=run_analysis)


risk_button = tk.Button(frame, text="Risk Report", bg="white", width=20, height=2, command=navigate_to_page1)
risk_button.pack(side="left", padx=10)

hist_button = tk.Button(frame, text="Histogram Report", bg="white", width=20, height=2, command=navigate_to_page2)
hist_button.pack(side="right", padx=10)

label = tk.Label(root, text="EPB Transformer Load Analysis", bg="black", fg="white")
label.pack(pady=20)

home_button = tk.Button(root, text="Home", bg="white", width=10, height=2, command=navigate_to_home)

selection_label = tk.Label(root,bg="black", fg="white", text="Account for EV's? If so, how many?")
'''
# Add Yes or No Radiobutton
choice_frame = tk.Frame(root, bg="black")
choice_label = tk.Label(choice_frame, text="Account for EV's?", bg="black", fg="white")
choice_var = tk.StringVar(value="Yes")
yes_button = tk.Radiobutton(choice_frame, text="Yes", variable=choice_var, value="Yes", bg="black", fg="white", indicatoron=False, selectcolor="green", font=("Arial", 12))
no_button = tk.Radiobutton(choice_frame, text="No", variable=choice_var, value="No", bg="black", fg="white", indicatoron=False, selectcolor="red", font=("Arial", 12))
ev_count_label = tk.Label(choice_frame, text="# of EV's", bg="black", fg="white")
ev_count_entry = tk.Entry(choice_frame, width=10)
transformer_label = tk.Label(choice_frame, text="Transformer SID", bg="black", fg="white")
transformer_entry = tk.Entry(choice_frame, width=10)
runRisk_button = tk.Button(choice_frame, text="Run", bg="white", width=10, height=2, command=run_analysis)
'''
root.mainloop()