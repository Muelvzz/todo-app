import functions
import time
import FreeSimpleGUI as FGS

FGS.theme("DarkGreen5")

label_time = FGS.Text('', key='clock')
label1 = FGS.Text("Enter tasks for today: ")
input_box = FGS.InputText(tooltip='Type the task', key="todo")

list_box = FGS.Listbox(values=functions.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=[50, 7])

add_button = FGS.Button(image_source="complete.png")
edit_button = FGS.Button("Edit")
complete_button = FGS.Button("Complete")
Exit_button = FGS.Button("Exit")

window = FGS.Window("Muelvin's Today Lists", layout=[
                    [label_time],
                    [label1, input_box, add_button],
                    [list_box, edit_button, complete_button],
                    [Exit_button]],
                    font=("Arial", 15))

while True:
    event, value = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b-%d, %Y %H:%M:%S"))
    print(event)
    print(value)
    match event:

        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                FGS.popup("Select task to edit", font=('Arial', 10))
                # todos = functions.get_todos()
                # functions.write_todos(todos)
                # window['todos'].update(values=todos)

        case "Complete":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                # This is my personal code
                # index = todos.index(todo_to_complete)
                # todos.pop(index)
                # functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                FGS.popup("Select task to complete", font=('Arial', 10))

        case "todos":
            window['todo'].update(value=value['todos'][0])

        case "Exit":
            break

        case FGS.WIN_CLOSED:
            break
window.close()
