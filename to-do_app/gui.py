import functions
import _tkinter
import FreeSimpleGUI as FGS

label1 = FGS.Text("Enter tasks for today: ")
input_box = FGS.InputText(tooltip='Type the task', key="todo")
add_button = FGS.Button("Add")

list_box = FGS.Listbox(values=functions.get_todos(),
                       key="todos",
                       enable_events=True,
                       size=[45, 10])
edit_button = FGS.Button("Edit")

window = FGS.Window("Muelvin's Today Lists", layout=[
                    [label1, input_box, add_button],
                    [list_box, edit_button]],
                    font=("Arial", 15))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:

        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = value['todos'][0]
            new_todo = value["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=value['todos'][0])

        case FGS.WIN_CLOSED:
            break
window.close()
