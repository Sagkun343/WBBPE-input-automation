import tkinter as tk
from tkinter import Text
from ttkbootstrap import Window, Label, Frame, Entry, Button

import wbbpe_functions as gf

# Global Variables
student = 0
threshold = 20
num_array = []
start_coord = (0, 0)
end_coord = (0, 0)


# Functions
def button_press():
    global num_array
    entry_csv = text_input.get("1.0", tk.END)
    num_array = gf.csv_to_list_of_integers(entry_csv)
    csv_helper_output.config(text=str(gf.is_less_than_equals_value(numbers=num_array, threshold=threshold)))


def student_button_press():
    global student
    try:
        user_input = int(student_number_entry.get())
    except ValueError:
        sn_output.config(text="Try again.")
    sn_output.config(text=str(user_input))
    student = user_input


def threshold_command():
    try:
        user_threshold = int(threshold_entry.get())
    except ValueError:
        threshold_output.configure(text="Not a valid threshold.")
    if gf.is_less_than_equals_value(num_array, user_threshold)[0]:
        threshold_output.configure(text=f"Numbers valid.")
    else:
        threshold_output.configure(
            text=f"At least one number invalid. position: {gf.is_less_than_equals_value(num_array, user_threshold)[1] + 1}.")


def get_coordinates_start():
    global start_coord
    start_coord = gf.get_mouse_location()
    coord_output.configure(text='starting coordinate set.')


def get_coordinates_end():
    global end_coord
    end_coord = gf.get_mouse_location()
    coord_output.configure(text='ending coordinates set.')


def final_button_press():
    gf.print_all(students=student, start_coord=start_coord, end_coord=end_coord, sleep_time=10, num_arr=num_array)


# Create the main window
window = Window(themename='litera')
width, height = 1600, 900
window.title("WBBPE Web Helper")
window.geometry(f"{width}x{height}")

# Introduction
Introduction = Label(master=window,
                     text="Steps to help yourself:\nStep 1. Open your preferred browser.\nStep 2. Have all the "
                          "marks in a csv format.\nStep 3. Enter the number of students (must be positive digits;"
                          " no points)\nStep 4. Enter the marks.",
                     font="Calibri 12", justify="left")
Introduction.pack(pady=5, side='top')

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
csv_frame = Frame(master=window)
csv_helper = Label(master=csv_frame,
                   text="Enter Your marks Here.", font="Calibri 12 italic", justify="center")
text_input = Text(master=csv_frame, height=10, width=100)
csv_button = Button(master=csv_frame, text="Press me!", command=button_press)
csv_helper.pack()
text_input.pack()
csv_helper_output = Label(master=csv_frame)
csv_helper_output.pack(side='bottom', pady=5)
csv_button.pack(pady=5)
csv_frame.pack(padx=5)

# Check numbers section
threshold_frame = Frame(master=window)
threshold_Label = Label(master=threshold_frame, text="Max. marks allowed:", justify='left')
threshold_entry = Entry(master=threshold_frame, width=10)
threshold_button = Button(master=threshold_frame, text='threshold (custom)', command=threshold_command)
threshold_output = Label(master=window)
threshold_Label.pack(padx=5, side='left')
threshold_entry.pack(padx=5, side='left')
threshold_button.pack(padx=5, side='right')
threshold_frame.pack(padx=5, pady=5)
threshold_output.pack(pady=5, padx=5)

# start coordinate section:
coord_frame = Frame(master=window)
coord_Label = Label(master=coord_frame,
                    text="Press here and go to first marks position. wait for 5 secs for completion.")
coord_button_start = Button(master=coord_frame, text='starting_coord', command=get_coordinates_start)

coord_Label.pack(padx=5, side='left')
coord_button_start.pack(padx=5, side='left')
coord_frame.pack(padx=5, pady=5)

# end coord section:
coord_frame_end = Frame(master=window)
coord_Label_end = Label(master=coord_frame_end,
                        text="Press here and go to last marks position. wait for 5 secs for completion.")
coord_button_end = Button(master=coord_frame_end, text='ending_coord', command=get_coordinates_end)
coord_output = Label(master=window)
coord_Label_end.pack(side='left')
coord_button_end.pack(padx=5, side='left')
coord_output.pack(pady=5)
coord_frame_end.pack(padx=5, pady=5)

# Final Button Section
final_button = Button(master=window, text="START", command=final_button_press, width=10)
final_button.pack(pady=15, padx=15)

# Run
if __name__ == '__main__':
    window.mainloop()
    
