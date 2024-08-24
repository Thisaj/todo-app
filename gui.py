
import modules.cli as functionsss
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme('NeonBlue1')

clock = sg.Text("", key="CLOCK")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button(key="Add",image_size=(100,100), image_source="add.png", button_color="white", mouseover_colors="red")
list_box = sg.Listbox(values=functionsss.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
edit_bottun= sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do app",
                   layout=[
                       [clock],
                       [label],
                       [input_box, add_button],
                       [list_box, edit_bottun, complete_button],
                       [exit_button]
                   ],
                   font=("Helvetica", 20),)

while True:
    event, values=window.read(timeout=10)
    window["CLOCK"].Update(value=time.strftime("%c"))
    # print(event, values)
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case "Add":
            todos = functionsss.get_todos()
            new_todo=values['todo'] +"\n"
            todos.append(new_todo)
            functionsss.set_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case "Edit":
            try:
                todo_to_edit=values['todos'][0]
                new_todo = values['todo']
                todos = functionsss.get_todos()
                index= todos.index(todo_to_edit)
                print("new todo", new_todo)
                todos[index]= new_todo
                functionsss.set_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select a name")
        case "Complete":
            try:
                todo_to_complete=values['todos'][0]
                todos = functionsss.get_todos()
                todos.remove(todo_to_complete)
                functionsss.set_todos(todos)
                window['todo'].update(value="")
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select a name")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            exit()

window.close()
