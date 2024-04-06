import PySimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todo.txt"):
    with open("todo.txt", "w") as file:
        pass

sg.theme("black")

label = sg.Text("Type a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo", font="Helvetica")
add_button = sg.Button("Add")

edit_button = sg.Button("Edit")
output_box = sg.Listbox(values=functions.to_get_todo(), key="todos", size=(45, 10), enable_events=True)

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

clock = sg.Text(time.strftime("%d/%b/%Y, %H:%M:%S"), key="clock")

window = sg.Window("My todo list", layout=[[clock], [label], [input_box, add_button],
                                           [output_box, edit_button, complete_button], [exit_button]])

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%d/%b/%Y, %H:%M:%S"))
    print(event, values)

    match event:
        case "Add":
            todos = functions.to_get_todo()
            todo_to_add = values["todo"]
            todos.append(todo_to_add + "\n")
            functions.to_write_todo(todos)
            window["todos"].update(values=todos)

        case "Edit":
            todos = functions.to_get_todo()
            todo_to_remove = values["todos"][0]
            todo_to_add = values["todo"] + "\n"
            index = todos.index(todo_to_remove)
            todos[index] = todo_to_add
            functions.to_write_todo(todos)
            window["todos"].update(values=todos)

        case "Complete":
            todos = functions.to_get_todo()
            todo_to_remove = values["todos"][0]
            index = todos.index(todo_to_remove)
            todos.pop(index)
            functions.to_write_todo(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WINDOW_CLOSED:
            break
window.close()