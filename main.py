import tkinter as tk
from tkinter import Text
from ttkbootstrap import Window, Label, Frame, Entry, Button

import wbbpe_functions as gf

# Global Variables
student = 0
num_array = []


# Functions
def button_press():
    global num_array
    entry_csv = text_input.get("1.0", tk.END)
    num_array = gf.csv_to_list_of_integers(entry_csv)
    output_widget.config(text=str(gf.is_less_than_equals_value(numbers=num_array, threshold=20)))


def student_button_press():
    global student
    try:
        user_input = int(student_number_entry.get())
    except ValueError:
        sn_output.config(text="Try again.")
    sn_output.config(text=str(user_input))
    student = user_input


def final_button_press():
    gf.print_all(students=student, start_coord=(602, 285), end_coord=(1641, 905), sleep_time=10, num_arr=num_array)


# Create the main window
window = Window(themename='darkly')
width, height = 1600, 900
window.title("WBBPE Web Helper")
window.geometry(f"{width}x{height}")

# Introduction
Introduction = Label(master=window,
                     text="Steps to help yourself:\nStep 1. Open your preferred browser.\nStep 2. Have all the "
                          "marks in a csv format.", font="Calibri 12", justify="center")
Introduction.pack(pady=5)

# Student Number Section
student_number = tk.IntVar()
student_number_frame = Frame(master=window)
student_number_label = Label(master=student_number_frame, text="Enter number of Students:-", justify="left")
student_number_entry = Entry(student_number_frame, width=30)
student_number_button = Button(master=student_number_frame, text="Enter", command=student_button_press)
sn_output = Label(master=student_number_frame)

student_number_label.pack(side='left', padx=5)
student_number_entry.pack(side='left', padx=5)
student_number_button.pack(side='right', padx=5)
sn_output.pack(side='bottom')
student_number_frame.pack()

# CSV Helper Section
csv_helper = Label(master=window,
                   text="Enter Your marks Here.", font="Calibri 12 italic", justify="center")
csv_helper.pack(pady=5)

# Text Input Widget
text_input = Text(master=window, height=10, width=100)
text_input.pack()

# Button Section
button = Button(master=window, text="Press me!", command=button_press)
button.pack(pady=10)

# Output Section
output_widget = tk.Label(window, height=10, width=100)
output_widget.pack(pady=10)

# Final Button Section
final_button = Button(master=window, text="START", command=final_button_press, width=10)
final_button.pack(pady=15, padx=15)

# Run
if __name__ == '__main__':
    window.mainloop()
