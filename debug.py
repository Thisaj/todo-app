# filenames = ["1.raw date.txt", "2.reports.txt"]
# for filename in filenames:
#     filename = filename.replace( ".", "-", 1 )
#     print(filename)
# from compressor import window

# menu = ["pasta", "pizza", "salad"]
# user_choice = int(input("enter the index of the item: "))     int
# message = f"you chose {menu[user_choice]}."
# print(message)


# menu = ["pasta", "pizza", "salad"]
# for i, j in enumerate(menu):            []    ()
#     print(f"{i}.{j}")



# 2222
# temperatures = [10, 12, 14]
# file = open("file.txt", "w")
# file.writelines(map(lambda x: str(x) + '\n', temperatures))
# file.close()

# 1111
# temperatures = [10, 12, 14]
# file = open("file.txt", "w")
# temperatures = [str(i) + "\n" for i in temperatures]
# file.writelines(temperatures)


# numbers = [10.1, 12.3, 14.7]
# numbers = [int(number) for number in numbers]        item)))))))number
# print(numbers)


# with open("file.txt", 'r') as file:
#     content = file.read()             کد صحیح
#     print(content)
#     print(len(content))


# with open("file.txt, 'r") as file:        کد مشکل دار
#     print(file.read())
#     print(len(file.read()))


# 11
# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#     return maximum
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)


# waiting_list = ["john", "mary"]
# try:
#     name = input("enter name: ")
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
# except ValueError:
#     print(f"{name} is not in the list")


# 11
# def speed(distance, time):
#     return distance/time
# print(speed(200, 4))


# 12
# def speed(distance, time):
#     return distance/time
# print(speed(300, 5))


# 6
# ids = ["XF345_89", "XER76849", "XA454_55"]
# x = 0
# for id in ids:
#     if'_' in id:
#         x = x + 1
# print(x)


# 8
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
# perimeter = (length + width)*2
# area = length * width
# print(f"perimeter is {perimeter}")
# print("area is", area)
# if perimeter < 14 and area < 8:
#     print("ok")
# else:
#     print("not ok")


# songs = ['take me back to eden', 'alkaline', 'ascensionism']
# f"this is the playlist: {", ".join(songs)}"


# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
# time = calculate_time(100)
# print(time)



# import modules.functions
#
# nr_of_periods = modules.functions.count("trees are good. grass is green.")
# print(nr_of_periods)


# from modules.functions import count
#
# nr_of_periods = count("trees are good. grass is green.")
# print(nr_of_periods)


# import PySimpleGUI as sg
#
# label = sg.Text('what are dolphins?')
# option1 = sg.Radio('amphibians', 'question1')
# option2 = sg.Radio('fish', 'question1')
# option3 = sg.Radio('mammals', 'question2')
# option4 = sg.Radio('birds', 'question2')
# window = sg.Window('file compressor', [[label],
#                    [option1],
#                     [option2],
#                     [option3],
#                     [option4],])
# window.read()
# window.close()

import PySimpleGUI as sg
label= sg.Text('Kilometers')
input_box = sg.InputText(tooltip='Enter Kilometers')
convert_button = sg.Button("Convert")

window = sg.Window('km to miles converter', layout=[
    [label,input_box],
      [convert_button]])

while True:
    event, values = window.read()
    match event:
        case "convert":
            km = values["kms"]
            result = km_to_miles(km)
            window["output"].update(value=result)
        case sg.Win_closed:
            break
window.close()
