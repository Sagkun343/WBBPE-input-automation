from pyautogui import moveTo, click, typewrite
from time import sleep, time

marks_array = [15, 13, 13, 17, 18,
               13, 11, 11, 16, 15,
               15, 14, 14, 18, 17,
               7, 6, 6, 13, 10,
               15, 13, 13, 18, 18,
               10, 10, 10, 15, 16,
               14, 12, 12, 15, 17,
               10, 10, 10, 12, 14,
               18, 16, 15, 17, 18,
               12, 11, 11, 15, 14,
               10, 10, 10, 15, 13,
               15, 14, 14, 17, 15,
               15, 14, 14, 18, 18,
               13, 15, 15, 14, 15,
               12, 10, 10, 12, 13,
               18, 16, 16, 18, 17,
               12, 10, 10, 15, 15,
               19, 17, 17, 15, 15,
               14, 12, 12, 17, 17,
               8, 5, 5, 10, 10,
               10, 7, 7, 10, 12,
               15, 13, 13, 15, 15,
               18, 16, 16, 13, 14,
               18, 17, 17, 18, 17,
               12, 10, 10, 12, 14,
               15, 15, 15, 16, 15,
               10, 10, 8, 12, 10,
               15, 12, 12, 13, 14,
               10, 9, 9, 12, 11,
               12, 10, 10, 12, 13,
               10, 12, 8, 14, 12,
               8, 7, 7, 15, 10,
               13, 13, 10, 14, 13,
               14, 10, 10, 13, 15,
               10, 8, 8, 12, 13,
               9, 7, 7, 10, 12,
               12, 10, 10, 14, 14,
               17, 15, 15, 13, 15,
               8, 7, 7, 10, 12,
               12, 10, 12, 16, 15,
               15, 15, 15, 16, 15,
               13, 12, 12, 15, 17]


def print_all(students: int, start_coord: tuple[float, float], end_coord: tuple[float, float],
              num_arr: list[int], subjects: int = 5, sleep_time: int = 5) -> None:
    start_time = time() # takes a snapshot of the current time of the program.
    sleep(sleep_time)
    print(f"You have {sleep_time} seconds. switch to the browser!")
    target_y = start_coord[1] # end position of Y - axis.
    gap_x = (end_coord[0] - start_coord[0]) / (subjects - 1)   # calculates the gap between two cells.
    gap_y = (end_coord[1] - start_coord[1]) / (students - 1)   # calculates the gap between two cells.
    num_ptr = 0   # number_array pointer.
    for k in range(students):
        for i in range(subjects):
            target_x = start_coord[0]  # makes sure the x-axis is reset.
            moveTo(target_x, target_y, duration=0.0)    # moves mouse cursor to position.
            click(button='left')   # simulates click so the text box is now actually working as intended.
            typewrite(str(num_arr[num_ptr]))    # writes into the text box.
            num_ptr += 1
            target_x += gap_x
        target_y += gap_y   # makes sure the Y-axis is incremented now that the nested loops over.
    end_time = time()
    print(f"All numbers printed successfully in {end_time - start_time} seconds.")


print_all(students=42, start_coord=(606, 162), end_coord=(1646, 982), num_arr=marks_array)


if __name__ == '__main__':
    pass
    # number_of_students: int = int(input("Enter first position(enter number only):"))
    # cell_pos_start_x: int = int(input("Enter first position(enter number only):"))
    # cell_pos_start_y: int = int(input("Enter first position(enter number only):"))
    # cell_pos_end_x: int = int(input("Enter first position(enter number only):"))
    # cell_pos_end_y: int = int(input("Enter first position(enter number only):"))
