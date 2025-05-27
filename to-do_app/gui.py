import functions
import _tkinter
import FreeSimpleGUI as FGS

label = FGS.Text("Enter tasks for today: ")
input_box = FGS.InputText(tooltip='Type the task')
add_button = FGS.Button("Add")

window = FGS.Window("Muelvin's Today Lists", layout=[
                    [label], [input_box, add_button]])
window.read()
window.close()
