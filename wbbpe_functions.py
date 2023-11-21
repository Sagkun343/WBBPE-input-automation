from pyautogui import moveTo, click, typewrite, position
from time import sleep, time
from typing import Tuple


def move_to_and_click(x: float, y: float) -> None:
    """Move the mouse cursor to the specified coordinates and click."""
    moveTo(x, y, duration=0.0)
    click(button='left')


def print_all(students: int, start_coord: Tuple[float, float], end_coord: Tuple[float, float],
              num_arr: list, subjects: int = 5, sleep_time: int = 5) -> None:
    start_time = time()
    print(f"You have {sleep_time} seconds. Switch to the browser!")
    sleep(sleep_time)

    if students == 1:
        gap_x = gap_y = 0
    else:
        gap_x = (end_coord[0] - start_coord[0]) / (subjects - 1)
        gap_y = (end_coord[1] - start_coord[1]) / (students - 1)

    num_ptr = 0

    for student in range(students):
        for subject in range(subjects):
            x_position = start_coord[0] + subject * gap_x
            y_position = start_coord[1] + student * gap_y

            move_to_and_click(x_position, y_position)
            typewrite(str(num_arr[num_ptr]))

            num_ptr += 1

    end_time = time()
    print(f"All numbers printed successfully in {end_time - start_time:.2f} seconds.")


def is_less_than_equals_value(numbers: list[int], threshold: int) -> tuple:
    for i in range(len(numbers)):
        if numbers[i] > threshold:
            return False, i

    return True, None


def csv_to_list_of_integers(csv: str) -> list[int]:
    """

    :rtype: object
    """
    res = []
    temp = str()
    num_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for num in csv:
        if num in num_set:
            temp += num
        elif num == ",":
            res.append(int(temp))
            temp = ""
        else:
            continue

    if temp:
        res.append(int(temp))

    return res


def get_mouse_location() -> Tuple:
    sleep(5)
    # Get the current mouse coordinates
    mouse_x, mouse_y = position()

    # Print the coordinates
    # print(f"Mouse Coordinates: X={mouse_x}, Y={mouse_y}")

    return mouse_x, mouse_y



